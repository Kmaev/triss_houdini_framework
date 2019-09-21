from __future__ import print_function
from triss import structure
import traceback
import json
import hou
import os
import imp
import re
import lucidity


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
    node.setColor(hou.Color((0.78, 0.41, 0.003)))
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
        if hou.isUIAvailable() is True:
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
    hipfile = hou.hipFile.name()

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
    read[asset_name]["versions"][version]["hipfile"] = hipfile
    read[asset_name]["versions"][version]['components'][file_format] = cache
    with open(project_file, 'w') as output_file:
        json.dump(read, output_file, indent=4)


def publish(node):
    cache_parm = node.parm("file_output")
    start_frame = int(node.parm("f1").eval())
    end_frame = int(node.parm("f2").eval() + 1)
    frame_range = range(start_frame, end_frame)
    json_data_publisher(node)
    cache_exists = cache_validator(node, "file_output", frame_range)
    if cache_exists is False:
        node.parm("execute").pressButton()
    if not cache_parm.isAtDefault():
        cache_parm.revertToAndRestorePermanentDefaults()
    hou.hipFile.saveAndIncrementFileName()


def reloadCache():
    node = hou.pwd()
    for child in node.children():
        for parm in child.parms():
            if parm.name() == "reload":
                parm.pressButton()


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


def get_version(node):  # used inside houdini to get max version for import geo
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
    try:
        cache_path = read[asset_name]["versions"][version]["components"][file_format]
    except Exception:
        return ''
    folder = os.environ.get("OUT")
    cache = os.path.join(folder, cache_path)
    cache = os.path.normpath(cache)
    cache = cache.replace('\\', '/')
    cache_path = cache
    return cache_path


def read_comment(node):
    file_index = node.parm("file_format").eval()
    file_format = node.parm("file_format").menuItems()[file_index]
    read = read_assets(node)
    asset_index = node.parm("name").eval()
    asset_name = node.parm("name").menuItems()[asset_index]
    version = str(node.parm("version").eval())
    try:
        comment = read[asset_name]["versions"][version]["description"]
    except Exception:
        return ''
    return comment


def onLoad_extract_data(node):
    context = node.parm('context').eval()
    context_data = context.split('/')
    project, sequence, shot, asset, version, file_format = context_data
    data = {'project': project, 'sequence': sequence, 'shot': shot,
            'name': asset, 'version': version, 'format': file_format}
    return data


def onLoad_create_path(node):
    try:
        data = onLoad_extract_data(node)
    except Exception:
        return ''

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
    publish_file = os.path.normpath(publish_file)
    publish_file = publish_file.replace('\\', '/')

    with open(publish_file, 'r') as read_file:
        file = json.load(read_file)
    asset = data["name"]
    version = str(int(data['version'].strip('v')))
    hipfile = file[asset]["versions"][version]['hipfile']
    comment = file[asset]["versions"][version]['description']
    display_comment = '{}\n\nPublished from scene: {}'.format(comment, hipfile)
    return display_comment


def updateRopNetwork(render_list):
    out = hou.node('/out')

    deadline = None
# check what nodes should be bypassed

    for child in out.children():
        if child.name() in render_list:
            bypass_inputs(child, render_list)
            bypass_outputs(child, render_list)
    for child in out.children():
        if child.name() in render_list:
            child.bypass(False)
# check if deadline node existes, if not create deadline node
        for output in child.outputs():
            if output.type().name() == 'deadline':
                deadline = output
                print(
                    "deadline found in child connected nodes. deadline is {}".format(deadline))
                break
        if deadline == None:
            if child.type().name() == 'deadline':
                deadline = child
                print("deadline found in out nodes {}".format(deadline))
    if deadline == None:
        deadline = out.createNode("deadline")
        print("deadline was created {}".format(deadline))

    deadline.bypass(False)
# connect to deadline
    disconnectInputs(deadline)
    for child in out.children():
        if child.name() in render_list:
            node = check_outputs(child)

            if node.path() == deadline.path():
                continue
            deadline.setNextInput(node)

    # deadline.parm("dl_Submit").pressButton()
    return hou.node(deadline.path())


def setDeadline(deadline_node):

    deadline_node.setCurrent(True)


def disconnectInputs(node):
    for connection in node.inputConnections():
        node.setInput(connection.inputIndex(), None)


def check_outputs(node):
    if not node.outputs():
        return node
    else:
        node = node.outputs()[0]
        return check_outputs(node)


def bypass_outputs(child, render_list):
    for node in child.outputs():
        if node not in render_list:
            node.bypass(True)
            bypass_outputs(node, render_list)


def bypass_inputs(child, render_list):
    for node in child.inputs():
        if node not in render_list:
            node.bypass(True)
            bypass_inputs(node, render_list)


def getFileContents(nodes):

    functions = []
    code = 'import hou\n\n'
    for i, node in enumerate(nodes):
        shader_name = node.name()
        parent = node.parent().path()

        code += node.asCode(function_name=shader_name,
                            brief=True,
                            recurse=True)
        functions.append(shader_name)

        code += 'def load(parent):\n'
        for func in functions:
            code += '    {}(parent)\n'.format(func)

    file_contents = {"code": code, "functions": functions, "parent": parent}

    return file_contents


def getMetadataFile(gallery, name):
    out = os.environ.get("OUT")

    data = {"gallery": gallery, "name": name}
    metadata_file = os.path.join(
        out, structure.folder_structure("metadata", data))

    metadata_file = os.path.normpath(metadata_file)
    metadata_file = metadata_file.replace('\\', '/')
    return metadata_file


def save_nodes(gallery, name, nodes, description, preview=None):
    metadata_file = getMetadataFile(gallery=gallery,
                                    name=name)

    file_contents = getFileContents(nodes)

    publish_folder = os.path.dirname(metadata_file)
    if not os.path.isdir(publish_folder):
        os.makedirs(publish_folder)

    publish_file = os.path.join(publish_folder,
                                'nodes.py')
    with open(publish_file, 'w') as f:
        f.write(file_contents['code'])

    relative_path = os.path.relpath(publish_file, publish_folder)

    saveMetadata(metadata_file=metadata_file,
                 gallery=gallery,
                 group_name=name,
                 parent=file_contents["parent"],
                 description=description,
                 preview=preview,
                 code=relative_path,
                 tags=file_contents['functions'])


def getPreviewPath(gallery, name):
    metadata_file = getMetadataFile(gallery=gallery,
                                    name=name)
    publish_folder = os.path.dirname(metadata_file)
    preview_folder = os.path.join(publish_folder, 'preview')
    preview_file = os.path.join(preview_folder, '{}.$F.jpg'.format(name))
    # preview_file = os.path.normpath(preview_file)
    # preview_file = preview_file.replace('\\', '/')

    return preview_file


def saveMetadata(metadata_file, gallery, group_name, parent, description, preview, code,
                 tags):
    data = {"gallery": gallery,
            "group_name": group_name,
            "description": description,
            "preview": preview,
            "parent": parent,
            "code": code,
            "tags": tags}

    with open(metadata_file, "w") as f:
        json.dump(data, f, indent=4)


def load_nodes(gallery, name, parent, elements):
    # out = os.environ.get("OUT")
    # shaders_folder = os.path.join(out, 'shaders')

    # file = os.path.join(name, "nodes.py")
    # publish_file = os.path.join(shaders_folder, file)
    # publish_file = os.path.normpath(publish_file)
    # publish_file = publish_file.replace('\\', '/')

    metadata = getMetadataFile(gallery=gallery, name=name)
    with open(metadata, 'r') as read_file:
        read = json.load(read_file)
    code = read["code"]
    folder = os.path.dirname(metadata)
    publish_file = os.path.join(folder, code)

    mod = imp.load_source('temp', publish_file)

    for element in elements:
        func = getattr(mod, element)
        func(parent)


def getRenderTab():
    found = None

    for pane in hou.ui.panes():
        if found:
            break
        for tab in pane.tabs():
            if isinstance(tab, hou.IPRViewer):
                found = tab
                break

    return found


class OpenFile(object):
    def __init__(self):
        self.data = {"project": hou.getenv("PROJECT"),
                     "sequence": hou.getenv("SEQUENCE"),
                     "shot": hou.getenv("SHOT"),
                     "department": hou.getenv("DEPARTMENT")}
        self.user_folder = structure.folder_structure("user_folder", self.data)
        self.user_folder = os.path.normpath(self.user_folder)
        self.user_folder = self.user_folder.replace('\\', '/')

        self.user = os.getenv("USERNAME")

        self.user_tasks = {}
        for i in os.listdir(self.user_folder):
            self.user_tasks[i] = os.path.join(self.user_folder, i)


def getMaxVersion(scenes_folder, scene_name):
    max_version = 0
    for scene in os.listdir(scenes_folder):
        result = re.match(r'(.+)_(v\d{3})(.+)', scene)

        if not result:
            continue

        head, version, tail = result.groups()

        if head != scene_name:
            continue

        version = int(version.strip('v'))
        max_version = max(version, max_version)

    max_version += 1

    return max_version


def makeScenePath(scene_name):
    project = hou.getenv("PROJECT")
    sequence = hou.getenv("SEQUENCE")
    shot = hou.getenv("SHOT")
    department = hou.getenv("DEPARTMENT")
    data = {"project": project,
            "sequence": sequence,
            "shot": shot,
            "department": department,
            "name": scene_name,
            'version': 'v001',
            'ext': 'hip'}

    scene_path = structure.folder_structure("scene_path", data)
    scene_path = os.path.normpath(scene_path)
    scene_path = scene_path.replace('\\', '/')
    scenes_folder = os.path.dirname(scene_path)
    if not os.path.isdir(scenes_folder):
        return scene_path
    else:
        max_version = getMaxVersion(scenes_folder=scenes_folder,
                                    scene_name=data["name"])
        data['version'] = 'v{:03d}'.format(max_version)
        scene_path = structure.folder_structure("scene_path", data)
        scene_path = os.path.normpath(scene_path)
        scene_path = scene_path.replace('\\', '/')

        return scene_path


def saveScene(scene_path):
    if not os.path.isdir(os.path.dirname(scene_path)):
        os.makedirs(os.path.dirname(scene_path))
    hou.hipFile.save(scene_path)


def sceneVersionUp():
    current_hip = hou.hipFile.name()
    scenes_folder = os.path.dirname(current_hip)
    template = lucidity.Template(
        'model', r"{mount_point:.+}/{project:[\w\d_]+}/{sequence:[\w\d_]+}/{shot:[\w\d_]+}/{department:.+}/scenes/{username:\w+}/{name:[\w\d_]+}/{name:[\w\d_]+}_{version:v\d+}.{ext:\w+}")
    data = template.parse(current_hip)

    max_version = getMaxVersion(scenes_folder=scenes_folder,
                                scene_name=data["name"])

    data['version'] = 'v{:03d}'.format(max_version)
    scene_path = structure.folder_structure("scene_path", data)
    scene_path = os.path.normpath(scene_path)
    scene_path = scene_path.replace('\\', '/')
    hou.hipFile.save(scene_path)


def setFrameRange():
    hou.setFps(25)
    hou.playbar.setFrameRange(1001, 1050)
    hou.playbar.setPlaybackRange(1001, 1050)
    hou.setFrame(1001)


def scene_was_loaded(event_type):
    if event_type == hou.hipFileEventType.AfterClear:
        setFrameRange()


class PublishableRenderRopNode(object):
    output_template = 'render_output'

    def __init__(self, node, name):
        self.name = name
        self.node = node

    def getProjectData(self):
        data = {}
        data['project'] = os.getenv('PROJECT')
        data['sequence'] = os.getenv('SEQUENCE')
        data['shot'] = os.getenv('SHOT')
        data['name'] = self.name
        data['version'] = 'v001'
        data['padding'] = '$F4'
        data['out'] = os.getenv('OUT')

        data['version'] = 'v' + str(self.getNextVersion(data)).zfill(3)
        return data

    def outputPath(self, template, data):
        path = structure.folder_structure(template, data)
        path = os.path.join(data['out'], path)
        path = os.path.normpath(path)
        path = path.replace('\\', '/')
        return path

    def getNextVersion(self, data):
        path = self.outputPath(template=self.output_template,
                               data=data)

        folder = os.path.dirname(path)
        if not os.path.isdir(folder):
            return 1

        max_version = 0
        render_task_folder = os.path.dirname(folder)
        for version in os.listdir(render_task_folder):
            result = re.match(r'(v)(\d{3})', data['version'])

            if not result:
                continue

            head, version = result.groups()

            max_version = max(int(version), max_version)

        max_version += 1
        return max_version

    def updateParameters(self):
        pass


class ArnoldPublishableRopNode(PublishableRenderRopNode):
    def updateParameters(self):
        self.node.parm('ar_picture').set(self.outputPath())
        self.node.parm('ar_picture_format').set('deepexr')


class MantraPublishableRopNode(PublishableRenderRopNode):
    def updateParameters(self):
        self.node.parm('ar_picture').set(self.outputPath())
        self.node.parm('ar_picture_format').set('deepexr')


def get_node(node, name):
    if 'arnold' in node.type().name():
        return ArnoldPublishableRopNode(node, name)
