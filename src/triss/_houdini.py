from __future__ import print_function
from triss import structure
import traceback
import json
import hou
import os



def create_node(name, context, node_type, position):
    new_node = hou.node(context).createNode(node_type, name)
    new_node.setPosition(position)
    return new_node


def extract_node_data(node):
    data = {}
    for parm in node.parms():
        if parm.name().startswith("data_"):
            name = parm.name().split("_")[1]
            if name == "data_format":
                data[name] = parm.menuItems()[parm.eval()]
            else:
                data[name] = parm.eval()
    if data.get('version'):
        if not isinstance(data['version'], str):
            version = "v{}".format(str(data['version']).zfill(3))
            data['version'] = version

    return data


def create_rop_node(node):
    geo = create_node(name='{}_geo'.format(node.name()),
                      context='/out',
                      node_type='out_bake_geo',
                      position=node.parent().position() - hou.Vector2(-1, - 1))
    reference_object = "{}/OUT".format(node.path())

    reference_path = geo.path()
    node.setParms({"rop_link": reference_path})
    geo.setParms({"sop_path": reference_object})


def update_name(node, rename=True, force_suffix=True):
    sop_path = node.node(node.parm("sop_path").eval()).parent()
    name = sop_path.name() + "_geo"
    if rename:
        node.setName(name)
    if not node.name().endswith('_geo') and force_suffix:
        node.setName(node.name() + '_geo')

def get_output_path(node):
    data = extract_node_data(node)
    template = node.parm("template").eval()

    menu_index = node.parm("data_format").eval()
    file_format = node.parm("data_format").menuItems()[menu_index]

    if file_format.lower() == 'abc':
        data['padding'] = ''
    else:
        data['padding'] = '$F4.'
    data["format"] = file_format  # overwrite format from index to token value

    output_path = structure.folder_structure(template, data)
    return output_path

def get_rop_output_path(rop):
    
    output_path = get_output_path(rop)
    folder = os.environ.get("OUT")
    cache = os.path.join(folder, output_path)
    cache = os.path.normpath(cache)
    cache = cache.replace('\\', '/')
    return cache


def render_version_up():
    node = hou.pwd().parent()

    cache_folder = get_rop_output_path(node)
    if os.path.isdir(os.path.dirname(cache_folder)):
        text = "Cache is already exists, do overwrite?"
        user_response = hou.ui.displayMessage(
            text, buttons=('Overwrite', 'Version Up', 'Cancel'))
        if user_response == 0:
            node.parm("execute").pressButton()
        if user_response == 1:
            version = node.parm("data_version")
            version = int(version.eval()) + 1
            node.setParms({"data_version": version})
        if user_response == 2:
            raise RuntimeError('Component already exists')

    cache_parm = node.parm("file_output")
    if not cache_parm.isAtDefault():
        cache_parm.revertToAndRestorePermanentDefaults()


def cache_validator(node, cache_parm, frame_range):
    cache = get_rop_output_path(node)
    cache_parm = node.parm(cache_parm)

    if os.path.isdir(os.path.dirname(cache)):
        for i in frame_range:
            cache_per_frame = cache_parm.evalAtFrame(i)
            if not os.path.isfile(cache_per_frame):
                return False
        return True
    return False


def json_data_publisher(node):
    data = extract_node_data(node)
    project_file = structure.publish_path(data)
    folder = os.path.dirname(project_file)
    if not os.path.isdir(folder):
        os.makedirs(folder)

    if not os.path.isfile(project_file):
        with open(project_file, "w") as f:
            f.write('{}')
    version = str(int(data['version'].strip('v')))

    asset_name = node.parm("data_name").eval()
    comment = node.parm("comment").eval()

    menu_index = node.parm("data_format").eval()
    file_format = node.parm("data_format").menuItems()[menu_index]
    cache = get_output_path(node)

    with open(project_file, "r") as read_file:
        read = json.load(read_file)
    if asset_name not in read:
        read[asset_name] = {"versions": {}}

    if version not in read[asset_name]["versions"]:
        read[asset_name]["versions"][version] = {'components': {}}

    else:
        if version in read[asset_name]["versions"]:
            text = "Version already exists, do you want to overwrite it?"
            user_response = hou.ui.displayMessage(
                text, buttons=('Overwrite', 'Version Up', 'Cancel'))
            if user_response == 0:
                if file_format not in read[asset_name]["versions"][version]["components"]:
                    read[asset_name]["versions"][version] = {'components': {}}

            if user_response == 1:
                all_versions = [int(x) for x in read[asset_name]["versions"]]
                # print(all_versions)
                version = str(max(all_versions) + 1)

                read[asset_name]["versions"][version] = {'components': {}}
                node.parm("data_version").set(int(version))

            if user_response == 2:
                raise RuntimeError('Component already exists')

    read[asset_name]["versions"][version]["description"] = comment
    read[asset_name]["versions"][version]['components'][file_format] = cache
    with open(project_file, 'w') as output_file:
        json.dump(read, output_file, indent=4)


def publish(node):
    cache_parm = node.parm("file_output")
    start_frame = int(node.parm("start_endx").eval())
    end_frame = int(node.parm("start_endy").eval() + 1)
    frame_range = range(start_frame, end_frame)
    json_data_publisher(node)
    cache_exists = cache_validator(node, "file_output", frame_range)
    print(cache_exists)
    if cache_exists is False:
        node.parm("execute").pressButton()
    if not cache_parm.isAtDefault():
        cache_parm.revertToAndRestorePermanentDefaults()


def catch_menu_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            traceback.print_exc()
            return []

    return wrapper


def read_assets(node):
    data = extract_node_data(node)
    path = structure.publish_path(data)
    # should I have nest two lines inside the publish_path function
    path = os.path.normpath(path)
    publish_file = path.replace('\\', '/')
    with open(publish_file) as read_file:
        read = json.load(read_file)

    return read


@catch_menu_exceptions
def create_menu(assets):
    result = []
    for asset in assets:
        # houdini menu expects two values, like "Token" "value" 
        # thats why we should append twice
        result.append(asset)
        result.append(asset)
    return result


def create_assets_menu(node):
    assets = read_assets(node).keys()
    assets_list = create_menu(assets)
    return assets_list


def get_version(node):
    read = read_assets(node)
    asset_index = node.parm("name").eval()
    asset_name = node.parm("name").menuItems()[asset_index]
    all_versions = [int(x) for x in read[asset_name]["versions"]]
    max_version = str(max(all_versions))
    return max_version


def create_cache_path(node):
    file_index = node.parm("file_format").eval()
    file_format = node.parm("file_format").menuItems()[file_index]
    read = read_assets(node)
    asset_index = node.parm("name").eval()
    asset_name = node.parm("name").menuItems()[asset_index]
    version = str(node.parm("version").eval())
    cache_path = read[asset_name]["versions"][version]["components"][file_format]
    return cache_path

def onLoad_extract_data(node):
    context = node.parm('context').eval()
    context_data = context.split('/')
    project, sequence, shot, asset , version, file_format = context_data
    data = {'project': project, 'sequence' : sequence, 'shot': shot, 'name': asset, 'version': version, 'format': file_format}
    return data

def onLoad_create_path(node):
    data = onLoad_extract_data(node)
    if data['format'].lower() == 'abc':
        data['padding'] = ''
    else:
        data['padding'] = '$F4.'
 # overwrite format from index to token value

    output_path = structure.folder_structure("cache_output", data)
    folder = os.environ.get("OUT")
    cache = os.path.join(folder, output_path)
    cache = os.path.normpath(cache)
    cache = cache.replace('\\', '/')
    return cache

def onLoad_set_path(node):
    cache = onLoad_create_path(node)
    node.parm('file').set(cache)

def change_switch(node):
    if node.parm('context').eval().endswith("abc"):
        switch = 0
    else:
        switch = 1
    return switch

def onLoad_read_comment(node):
    data = onLoad_extract_data(node)
    publish_file = structure.publish_path(data)
    with open(publish_file, 'r') as read_file: 
        file = json.load(read_file)
    asset = data["name"]
    version =  str(int(data['version'].strip('v')))
    comment = file[asset]["versions"][version]['description']
    return comment
