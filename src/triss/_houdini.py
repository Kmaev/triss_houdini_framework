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
    geo.setParms({"sop_path": reference_object})
    update_node_data(geo)
    reference_path = geo.path()

    node.setParms({"rop_link": reference_path}) #"load_from_disk":'`chs("{}/file_output")`'.format(reference_path) 


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


def update_node_data(node, rename=True, force_suffix=True):
    sop_path = node.node(node.parm("sop_path").eval()).parent()
    name = sop_path.name() + "_geo"
    if rename:
        node.setName(name)

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

    folder = os.environ.get("OUT")
    cache = os.path.join(folder, output_path)
    cache = os.path.normpath(cache)
    cache = cache.replace('\\', '/')
    node.setParms({"file_output": cache})

    if not node.name().endswith('_geo') and force_suffix:
        node.setName(node.name() + '_geo')
    return cache


def geo_publish(node):
    data = extract_node_data(node)
    project_file = structure.publish_path(data)
    folder = os.path.dirname(project_file)
    if not os.path.isdir(folder):
        os.makedirs(folder)
    
    if not os.path.isfile(project_file):
        with open(project_file, "w") as f:
            f.write('{}')

    asset_name = node.parm("data_name").eval()
    comment = node.parm("comment").eval()

    #versioning should be a separate  function
    version = node.parm("data_version").eval()
    if node.parm("auto_inc").eval() is True:  # Version auto inc
        version += 1
        node.setParms({"data_version": version})
    cache = update_node_data(node)
    version = str(version)

    menu_index = node.parm("data_format").eval()
    file_format = node.parm("data_format").menuItems()[menu_index]

    with open(project_file, "r") as read_file:
        read = json.load(read_file)

    if asset_name not in read:
        read[asset_name] = {"versions": {}}

    if version not in read[asset_name]["versions"]:
        read[asset_name]["versions"][version] = {'components': {}}
    else:
        if file_format in read[asset_name]["versions"][version]["components"]:
            text = "Component already exists, do you want to overwrite it?"
            user_response = hou.ui.displayMessage(text, buttons=('OK', 'Version Up', 'Cancel'))

            if user_response == 1:
                all_versions = [int(x) for x in read[asset_name]["versions"]]
                version = str(max(all_versions) + 1)
                read[asset_name]["versions"][version] = {'components': {}}
                node.parm("data_version").set(int(version))
                update_node_data(node)

            if user_response == 2:
                raise RuntimeError('Component already exists')


    read[asset_name]["versions"][version]["description"] = comment
    read[asset_name]["versions"][version]['components'][file_format] = cache

    with open(project_file, 'w') as output_file:
        json.dump(read, output_file, indent=4)


