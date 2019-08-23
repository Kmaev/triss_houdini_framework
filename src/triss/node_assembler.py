from __future__ import print_function, absolute_import

import hou
import os
from Qt import QtWidgets, QtCore
from triss.vendor import panel


class NodeAssembler(panel.BaseScrollablePanelWidget):
    def __init__(self, title, parent=None):
        super(NodeAssembler, self).__init__(title, parent=parent)


        self.node_layout = QtWidgets.QVBoxLayout()
        self.config_layout = QtWidgets.QHBoxLayout()
        self.help_layout = QtWidgets.QVBoxLayout()

        self.body_layout.addLayout(self.config_layout)
        self.body_layout.addLayout(self.node_layout)
        self.body_layout.addLayout(self.help_layout)

        self.list_label = QtWidgets.QLabel("Selected nodes (drag and drop to add):")
        self.list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.help_layout.addWidget(self.list_label)

        self.reset_button = QtWidgets.QPushButton("Reset Config", self)
        self.config_layout.addWidget(self.reset_button)
        self.reset_button.clicked.connect(self.resetConfig)

        self.save_button = QtWidgets.QPushButton("Save Config", self)
        self.config_layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.saveConfig)

        self.current_nodes = []
        self.buttons = []

        self.saved_nodes = hou.getenv("BUTTONS")
        if self.saved_nodes is not None:
            self.saved_nodes_list = self.saved_nodes.split(",")
            for item in self.saved_nodes_list:
                self.addNode(item)

        self.setAcceptDrops(True)


    def addNode(self, path):
        self.save_button.setEnabled(True)
        self.current_nodes.append(path)
        node_button = QtWidgets.QPushButton(path, self)
        node_button.clicked.connect(self.onNodeClicked)
        self.buttons.append(node_button)
        self.node_layout.addWidget(node_button)

    def dragEnterEvent(self, event):
        nodes = event.mimeData().text().split(',')
        nodes = [hou.node(x) for x in nodes]
        if any([x is None for x in nodes]):
            event.ignore()
        else:
            event.acceptProposedAction()

    def dropEvent(self, event):
        nodes = event.mimeData().text()

        for node in nodes.split(','):
            if node in self.current_nodes:
                continue

            self.addNode(node)

        event.acceptProposedAction()

    def onNodeClicked(self):
        button = self.sender()
        node = hou.node(button.text())
        node.setCurrent(True)


    def saveConfig(self):
        separator = ","
        value = separator.join(self.current_nodes)
        print(value)
        hou.hscript("setenv BUTTONS = {}".format(value)) #add env variable to houdini
        self.save_button.setEnabled(False)


    def resetConfig(self):
        hou.hscript("setenv BUTTONS = ''")
        while self.node_layout.count() > 0:
            item = self.node_layout.takeAt(0)
            if not item:
                continue
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.current_nodes = []
        self.buttons = []
        self.save_button.setEnabled(True)



def python_panel():
    return NodeAssembler('Node Assembler')
