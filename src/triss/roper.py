from __future__ import print_function, absolute_import
from triss import _houdini
from triss import res
import hou
import os
from Qt import QtWidgets, QtCore
from triss.vendor import panel

reload(panel)
reload(_houdini)

# class RoperDialog(QtWidgets.QDialog):


class RoperDialog(panel.BaseScrollablePanelWidget):
    def __init__(self, title, parent=None):
        super(RoperDialog, self).__init__(title = title, parent=parent)

        self.setObjectName('Roper')

        self.main_layout.setContentsMargins(5, 10, 5, 2)

        self.display_widget = QtWidgets.QWidget()

        self.name = QtWidgets.QLabel()
        self.name.setText("Choose ROP nodes to render")
        self.body_layout.addWidget(self.name)


        check_boxes_layout = QtWidgets.QVBoxLayout()
        check_boxes_layout.setContentsMargins(3, 20, 3, 20)
        self.display_widget.setLayout(check_boxes_layout)
        self.body_layout.addWidget(self.display_widget)


        self.checks = []
        self.deadline = None

        self.out_list = self.getRopNodes()
        for i in self.out_list:
            node_check_box = QtWidgets.QCheckBox(i)
            check_boxes_layout.addWidget(node_check_box)
            self.checks.append(node_check_box)

        self.load_button = QtWidgets.QPushButton("Load", self)
        self.body_layout.addWidget(self.load_button)

        self.dl_button = QtWidgets.QPushButton("Go To Deadline", self)
        self.body_layout.addWidget(self.dl_button)

        self.render_button = QtWidgets.QPushButton("Render", self)
        self.body_layout.addWidget(self.render_button)

        self.dl_button.clicked.connect(self.goToDeadline)
        self.load_button.clicked.connect(self.onLoad)
        self.render_button.clicked.connect(self.onRender)
        for i in self.checks:
            i.clicked.connect(self.loadBtn)

        self.load_button.clicked.connect(self.onLoad)

        style_folder = os.environ.get("STYLE_TRISS")
        with open(os.path.join(style_folder, "style_hou.qss"), 'r') as f:
            style = f.read()

        self.setStyleSheet(style)
        self.scroll.setStyleSheet(style)
        self.display_widget.setStyleSheet(style)

    def renderList(self):
        return [x.text() for x in self.checks if x.isChecked()]

    def loadBtn(self):
        self.load_button.setEnabled(True)

    def onLoad(self):
        self.deadline = _houdini.updateRopNetwork(self.renderList())
        self.load_button.setEnabled(False)

    def goToDeadline(self):
        _houdini.setDeadline(self.deadline)

    def getRopNodes(self):
        out = hou.node('/out')
        out_nodes = []
        nodes_for_render = ["out_bake_geo", "geometry"]
        for i in out.children():
            if i.type().name() not in nodes_for_render:
                continue
            out_nodes.append(i.name())
        return out_nodes

    def onRender(self):
        self.deadline.parm("dl_Submit").pressButton()
        self.close()


dialog = None


def show_houdini():
    global dialog
    dialog = RoperDialog('Roper v0.1.6', parent=hou.qt.mainWindow())
    dialog.show()
    return dialog


def python_panel():
    return RoperDialog('Roper')
