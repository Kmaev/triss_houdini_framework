from __future__ import print_function
from triss import structure
import json
import hou
import os
reload(structure)


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


def get_rop_output_path(rop):
    data = extract_node_data(rop)
    template = rop.parm("template").eval()

    menu_index = rop.parm("data_format").eval()
    file_format = rop.parm("data_format").menuItems()[menu_index]

    if file_format.lower() == 'abc':
        data['padding'] = ''
    else:
        data['padding'] = '$F4.'
    data["format"] = file_format  # overwrite format from index to token value

    output_path = structure.folder_structure(template, data)

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
    cache = get_rop_output_path(node)

    with open(project_file, "r") as read_file:
        read = json.load(read_file)
    if asset_name not in read:
        read[asset_name] = {"versions": {}}

    if version not in read[asset_name]["versions"]:
        read[asset_name]["versions"][version] = {'components': {}}

    else:
        if file_format in read[asset_name]["versions"][version]["components"]:
            text = "Component already exists, do you want to overwrite it?"
            user_response = hou.ui.displayMessage(
                text, buttons=('Overwrite', 'Version Up', 'Cancel'))
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
