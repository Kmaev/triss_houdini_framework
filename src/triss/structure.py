from __future__ import print_function
import json
import os


def get_template(name):
    path = os.environ.get("FOLDER_STUCTURE_PATH")
    with open(path) as read_file:
        file = json.load(read_file)
    if name not in file.keys():
        raise ValueError('Template "{}" doesn\'t exist'.format(name))
    return file[name]


def folder_structure(template, data):
    template_data = get_template(name=template)
    template_data = os.path.expandvars(template_data)

    try:
        path = template_data.format(**data)
    except KeyError as e:
        raise RuntimeError("Not enough template data, {} missed ".format(e))
    return path


def publish_path(data):
    folder = os.environ.get("OUT")
    path = folder_structure(template="publish_index", data=data)
    path = os.path.join(folder, path)
    return path
