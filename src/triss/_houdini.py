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
    return data


def crete_rop_node(node):
    geo = create_node(name='{}_geo'.format(node.name()),
                      context='/out',
                      node_type='geometry',
                      position=node.parent().position() - hou.Vector2(-1, - 1))
    path = "{}/OUT".format(node.path())
    geo.setParms({"soppath": path})
    

