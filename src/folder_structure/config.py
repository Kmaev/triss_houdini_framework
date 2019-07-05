from __future__ import print_function
import json


def get_template(path, name):
    with open(path) as read_file:
        file = json.load(read_file)
    for i in file.keys():
        if name == i:
            data = file.get(name)
            return data
        else:
            raise ValueError('Template "{}" doesn\'t exist'.format(name))


def folder_structure(template, data):
    template_data = get_template(
        # change path for env variable?
        path=r"E:\code\learn\resources\config\folder_structure.json",
        name=template)

    path = template_data.format(project=data.get("project"),
                                sequence=data.get("sequence"),
                                shot=data.get("shot"),
                                name=data.get("name"),
                                version=data.get("version"))
    path_check = path.split("\\")
    for i in path_check:
        if i == "None":
            raise ValueError(
                "Not enough template data.\nTemplate: {},\nData: {} ".format(
                    template_data, data.values()))

    return path


