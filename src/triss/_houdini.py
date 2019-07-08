from __future__ import print_function
from structure import folder_structure
import hou


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
    output_path = folder_structure(template,data)
    node.setParms({"file_path":output_path})
    reference_path = '`chs("' + geo.relativePathTo(node) + '/file_path")`'
    geo.setParms({"soppath": reference_object, "sopoutput":reference_path})

