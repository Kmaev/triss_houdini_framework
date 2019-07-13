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
            data[name] = parm.eval()
    if data.get('version'):
        if not isinstance(data['version'], str):
            version = "v{}".format(str(data['version']).zfill(3))
            data['version'] = version
    return data


def create_rop_node(node):
    geo = create_node(name='{}_geo'.format(node.name()),
                      context='/out',
                      node_type='geometry',
                      position=node.parent().position() - hou.Vector2(-1, - 1))
    reference_object = "{}/OUT".format(node.path())
    template = node.parm("template").eval()
    data = extract_node_data(node)
    output_path = structure.folder_structure(template, data)
    node.setParms({"file_path": output_path})
    reference_path = '`chs("' + geo.relativePathTo(node) + '/file_path")`'
    geo.setParms({"soppath": reference_object, "sopoutput": reference_path})


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
    version = node.parm("data_version").eval()
    if node.parm("auto_inc").eval() == True:     ## Version auto inc
        version += 1
        node.setParms({"data_version": version})
    version = str(version) 
    folder = os.environ.get("OUT")
    menu_index = node.parm("format").eval()
    file_format =  node.parm("format").menuItems()[menu_index]

    cache = os.path.join(folder,node.parm("file_path").unexpandedString())
    create_rop_node(node) #update all data
    with open(project_file, "r") as read_file:
        read = json.load(read_file)

    if asset_name not in read:
        read[asset_name] = {"versions": {}}

    if version not in read[asset_name]["versions"]:
        read[asset_name]["versions"][version] = {'components': {}}


    read[asset_name]["versions"][version]["description"] = comment
    read[asset_name]["versions"][version]['components'][file_format] = cache



    with open(project_file, 'w') as output_file:
       json.dump(read, output_file, indent=4)
