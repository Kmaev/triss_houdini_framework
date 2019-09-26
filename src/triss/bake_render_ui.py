from __future__ import print_function
from Qt import QtWidgets
import hou
import os
import res
import flow_layout
from triss import _houdini


class BakeRenderDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(BakeRenderDialog, self).__init__(parent=parent)
        # self.resize(450,180)
        self.setWindowTitle("TRISS: Bake render v0.1.5")
        self.nodes_list = []
        self.phantom_selected_list = []
        self.render_nodes_to_create = []
        self.render_engines = {"arnold": "arnold", "mantra": "ifd"}
        self.possible_render_nodes = ['subnet', 'geo']
        self.render_cam = None
        self.start_pos = None

        self.central_layout = QtWidgets.QVBoxLayout(self)

        self.render_name_label = QtWidgets.QLabel('Type render name here:')
        self.central_layout.addWidget(self.render_name_label)

        self.render_name = QtWidgets.QLineEdit()
        self.render_name.setPlaceholderText("my_nice_new_render")
        self.central_layout.addWidget(self.render_name)

        self.render_list_label = QtWidgets.QLabel('Nodes to render:')
        self.central_layout.addWidget(self.render_list_label)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.flow_widget = QtWidgets.QWidget()
        self.flow_layout = flow_layout.FlowLayout()
        self.flow_widget.setLayout(self.flow_layout)
        self.scroll_area.setWidget(self.flow_widget)

        self.central_layout.addWidget(self.scroll_area)

        self.engines_label = QtWidgets.QLabel('Available render engines:')
        self.central_layout.addWidget(self.engines_label)

        self.render_engines_layout = QtWidgets.QHBoxLayout()
        self.central_layout.addLayout(self.render_engines_layout)
        self.addRenderEnginesSelection()

        self.update_render_button = QtWidgets.QPushButton('Update render list')
        self.central_layout.addWidget(self.update_render_button)

        self.update_render_button.clicked.connect(self.addRenderNodes)
        self.update_render_button.clicked.connect(self.populatePhantomList)

        self.phantom_label = QtWidgets.QLabel('Possible phantom objects:')
        self.central_layout.addWidget(self.phantom_label)

        self.phantom_list = QtWidgets.QListWidget()
        self.phantom_list.setSelectionMode(
            QtWidgets.QAbstractItemView.MultiSelection)
        self.central_layout.addWidget(self.phantom_list)

        self.phantom_list.itemClicked.connect(self.getSelection)

        self.camera_label = QtWidgets.QLabel("Camera selection:")
        self.central_layout.addWidget(self.camera_label)

        self.camera_combo = QtWidgets.QComboBox()
        self.camera_combo.currentIndexChanged.connect(
            self.onCameraComboChanged)
        self.central_layout.addWidget(self.camera_combo)

        self.make_render_node_button = QtWidgets.QPushButton('Add render node')
        self.make_render_node_button.clicked.connect(self.addRenderNode)
        self.central_layout.addWidget(self.make_render_node_button)

        self.addRenderNodes()
        self.populatePhantomList()
        self.populateCameraCombo()
        self.getStartRenderNodePos()

        style_folder = os.environ.get("STYLE_TRISS")
        style_file = os.path.join(style_folder, "style_hou.qss")
        with open(style_file, 'r') as f:
            style = f.read()
        self.setStyleSheet(style)

        if self.parent():
            self.parent().setStyleSheet(self.parent().styleSheet())

    def addRenderEnginesSelection(self):
        for render in self.render_engines.keys():
            checkbox = QtWidgets.QCheckBox(render)
            # checkbox.setProperty(self.render_engines.values())
            self.render_engines_layout.addWidget(checkbox)

    def getSelectedRenderEngine(self):
        self.render_nodes_to_create = []
        for i in range(self.render_engines_layout.count()):
            item = self.render_engines_layout.itemAt(i)
            widget = item.widget()
            if widget.isChecked():
                self.render_nodes_to_create.append(str(widget.text()))
        if len(self.render_nodes_to_create) <= 0:
            message = 'No render engine was selected'
            QtWidgets.QMessageBox.critical(self, 'Error', message)
            raise RuntimeError(message)

    def addRenderNodes(self):
        while self.flow_layout.count() > 0:
            item = self.flow_layout.takeAt(0)
            if not item:
                continue

            w = item.widget()
            if w:
                w.deleteLater()
        self.nodes_list = []
        not_to_render_list = []
        if not hou.selectedNodes():
            message = "Select nodes to render"
            parent = hou.qt.mainWindow()
            mbox = QtWidgets.QMessageBox.critical(parent, 'Error', message)
            raise RuntimeError

        for node in hou.selectedNodes():
            if node.type().name() in self.possible_render_nodes:
                self.nodes_list.append(node.name())
                node_label = QtWidgets.QLabel(node.name())
                node_label.setObjectName('render_label')
                self.flow_layout.addWidget(node_label)
            else:
                not_to_render_list.append(node.name())

        if len(not_to_render_list) > 0:
            message = "Selected nodes {} cannot be rendered".format(
                ', '.join(not_to_render_list))
            parent = hou.qt.mainWindow()
            mbox = QtWidgets.QMessageBox.information(parent, 'Info', message)

    def populatePhantomList(self):
        self.phantom_list.clear()
        for node in hou.node('/obj').children():
            if node.type().name() == 'geo' and node.name() not in self.nodes_list:
                self.phantom_list.addItem(node.name())

    def getSelection(self):
        self.phantom_selected_list = []
        selected = self.phantom_list.selectedItems()
        for widget in selected:
            self.phantom_selected_list.append(str(widget.text()))

    def populateCameraCombo(self):
        for node in hou.node('/obj').children():
            if node.type().name() == 'cam':
                self.camera_combo.addItem(node.name(), node.path())

    def onCameraComboChanged(self, index):
        sel = self.camera_combo.itemData(index)
        self.render_cam = sel

    def getStartRenderNodePos(self):
        out = hou.node('/out')
        pos_list = []
        if len(out.children()) > 0:
            for i in out.children():
                pos_list.append(i.position())
            max_x = max([x[0] for x in pos_list])

            max_y = max([x[1] for x in pos_list])

            self.start_pos = hou.Vector2(max_x + 2, max_y)
        else:
            self.start_pos = hou.Vector2(0, 0)

    def createRendersNodeToRop(self, render_name, to_render, to_phantom, render_engine, position):
        if not render_name:  # to show message
            message = 'Must specify render name'
            QtWidgets.QMessageBox.critical(self, 'Error', message)
            raise RuntimeError(message)  # to stop execute code

        out = hou.node('/out')
        render_node = out.createNode(render_engine, render_name)
        render_node.setPosition(position)
        render_node.setParms({'vobject': '', 'forceobject': to_render, 'phantom_objects': to_phantom,
                              'camera': self.render_cam})
        return render_node

    def addRenderNode(self):
        phantom = ', '.join(self.phantom_selected_list)
        render = ', '.join(self.nodes_list)
        self.getSelectedRenderEngine()
        for render_engine in self.render_nodes_to_create:
            node = self.createRendersNodeToRop(render_name=self.render_name.text(), to_render=render,
                                               to_phantom=phantom, render_engine=self.render_engines[render_engine], position=self.start_pos)
            render_node = _houdini.get_node(node, self.render_name.text())
            render_node.updateParameters()
            self.start_pos[1] -= 1
        self.close()


dialog = None


def show_houdini():
    import hou
    global dialog
    dialog = BakeRenderDialog(parent=hou.qt.mainWindow())
    dialog.show()
    return dialog
