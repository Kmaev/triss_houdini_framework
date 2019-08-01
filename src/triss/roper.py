from __future__ import print_function, absolute_import
from triss import _houdini
import hou
from triss.vendor.Qt import QtWidgets, QtCore
from triss.vendor import panel

reload(_houdini)

# class RoperDialog(QtWidgets.QDialog):


class RoperDialog(panel.BaseScrollablePanelWidget):
    def __init__(self, title, parent=None):
        super(RoperDialog, self).__init__(title, parent=parent)

        check_boxes_layout = QtWidgets.QVBoxLayout()
        self.body_layout.addLayout(check_boxes_layout)

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
    dialog = RoperDialog('Roper', parent=hou.qt.mainWindow())
    dialog.show()
    return dialog


def python_panel():
    return RoperDialog('Roper')
