from __future__ import print_function
from triss import structure
import sys
import json
import os
from triss.vendor.Qt import QtWidgets, QtCore


# class window(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.resize(500, 500)
#         self.setWindowTitle('What you want')

#         self.button_01 = QtWidgets.QPushButton("sometimes", self)
#         self.button_02 = QtWidgets.QPushButton("now", self)
#         self.edit = QtWidgets.QLineEdit("Write what you want here...")

#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.edit)
#         layout.addWidget(self.button_01)
#         layout.addWidget(self.button_02)

#         self.setLayout(layout)
#         self.button_01.clicked.connect(self.message_01)
#         self.button_02.clicked.connect(self.message_02)
#     def message_01(self):
#         print("you push {} button".format(self.button_01.text()))
#         print("you want  {} {}".format(self.edit.text(), self.button_01.text()))
#     def message_02(self):
#         print("you push {} button".format(self.button_02.text()))
#         print("you want  {}{}".format(self.edit.text(), self.button_02.text()))

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = window()
#     w.show()
#     sys.exit(app.exec_())


class ShotListDialog(QtWidgets.QDialog):
    def __init__(self, node, parent=None):
        super(ShotListDialog, self).__init__(parent=parent)

        project_file = os.environ.get("PROJECTS_INDEX_PATH")
        self.setWindowTitle('TRISS')
        self.node = node
        with open(project_file, "r") as read_file:
            self.read = json.load(read_file)

        self.shot_index = None

        self.project_list = QtWidgets.QListWidget(self)
        self.seq_list = QtWidgets.QListWidget(self)
        self.shot_list = QtWidgets.QListWidget(self)
        self.asset_list = QtWidgets.QListWidget(self)
        self.version_list = QtWidgets.QListWidget(self)
        self.component_list = QtWidgets.QListWidget(self)
        self.description_box = QtWidgets.QTextEdit(self)
        self.load_button = QtWidgets.QPushButton("Load", self)
        self.load_button.setEnabled(False)

        project_list = self.read.keys()
        for i in project_list:
            self.project_list.addItem(i)

        # self.project = self.project_list.selectedItems()[0].text()

        self.project_grp = QtWidgets.QGroupBox('Projects')
        self.project_grp_layout = QtWidgets.QHBoxLayout()
        self.project_grp.setLayout(self.project_grp_layout)
        self.project_grp_layout.addWidget(self.project_list)

        self.sequence_grp = QtWidgets.QGroupBox('Sequences')
        self.sequence_grp_layout = QtWidgets.QHBoxLayout()
        self.sequence_grp.setLayout(self.sequence_grp_layout)
        self.sequence_grp_layout.addWidget(self.seq_list)

        self.shot_grp = QtWidgets.QGroupBox("Shots")
        self.shot_grp_layout = QtWidgets.QHBoxLayout()
        self.shot_grp.setLayout(self.shot_grp_layout)
        self.shot_grp_layout.addWidget(self.shot_list)

        self.asset_grp = QtWidgets.QGroupBox('Assets')
        self.asset_grp_layout = QtWidgets.QHBoxLayout()
        self.asset_grp.setLayout(self.asset_grp_layout)
        self.asset_grp_layout.addWidget(self.asset_list)

        self.top_grp_layout = QtWidgets.QHBoxLayout()
        self.top_grp_layout.addWidget(self.project_grp)
        self.top_grp_layout.addWidget(self.sequence_grp)
        self.top_grp_layout.addWidget(self.shot_grp)

        self.version_grp = QtWidgets.QGroupBox('Versions')
        self.version_grp_layout = QtWidgets.QHBoxLayout()
        self.version_grp.setLayout(self.version_grp_layout)
        self.version_grp_layout.addWidget(self.version_list)

        self.component_grp = QtWidgets.QGroupBox('Components')
        self.component_grp_layout = QtWidgets.QVBoxLayout()
        self.component_grp.setLayout(self.component_grp_layout)
        self.component_grp_layout.addWidget(self.component_list)
        self.component_grp_layout.addWidget(self.description_box)

        self.bottom_grp_layout = QtWidgets.QHBoxLayout()
        self.bottom_grp_layout.addWidget(self.asset_grp)
        self.bottom_grp_layout.addWidget(self.version_grp)
        self.bottom_grp_layout.addWidget(self.component_grp)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(self.top_grp_layout)
        layout.addLayout(self.bottom_grp_layout)
        layout.addWidget(self.load_button)

        self.setLayout(layout)

        self.project_list.itemSelectionChanged.connect(self.onProjectChanged)
        self.seq_list.itemSelectionChanged.connect(self.onSequenceChanged)
        self.shot_list.itemSelectionChanged.connect(self.onShotChanged)
        self.asset_list.itemSelectionChanged.connect(self.onAssetChanged)
        self.version_list.itemSelectionChanged.connect(self.onVersionChanged)
        self.component_list.itemSelectionChanged.connect(
            self.onComponentChanged)

        self.load_button.clicked.connect(self.onLoad)

    def getSelection(self, widget):
        selected = widget.selectedItems()
        return selected[0].text() if selected else None

    def selectedProject(self):
        return self.getSelection(self.project_list)

    def selectedSequence(self):
        return self.getSelection(self.seq_list)

    def selectedShot(self):
        return self.getSelection(self.shot_list)

    def selectedAsset(self):
        return self.getSelection(self.asset_list)

    def selectedVersion(self):
        return self.getSelection(self.version_list)

    def selectedComponent(self):
        return self.getSelection(self.component_list)

    def onProjectChanged(self):
        self.seq_list.clear()

        project = self.selectedProject()

        if not project:
            return
        sequences = self.read[project]["sequences"]
        for i in sequences:
            self.seq_list.addItem(i)

    def onSequenceChanged(self):
        self.shot_list.clear()
        project = self.selectedProject()
        sequence = self.selectedSequence()

        if not sequence:
            # Clear the shot list
            return

        shots = self.read[project]["sequences"][sequence]["shots"]
        for i in shots:
            self.shot_list.addItem(i)

        # Same as the for loop
        # [self.shot_list.addItem(x) for x in shots]

    def onShotChanged(self):
        self.asset_list.clear()
        self.description_box.clear()
        project = self.selectedProject()
        sequence = self.selectedSequence()
        shot = self.selectedShot()

        if not sequence or not shot:
            self.shot_index = None
            return

        data = {"project": project,
                "sequence": sequence,
                "shot": shot}
        path = structure.publish_path(data)
        path = os.path.normpath(path)
        path = path.replace("\\", '/')
        try:
            with open(path, "r") as read_shot_index:
                shot_index = json.load(read_shot_index)
            self.shot_index = shot_index
        except IOError as e:
            self.description_box.setPlainText(
                "No published elements for this shot")
            raise RuntimeError("No published elements for this shot")

        assets = shot_index.keys()
        for i in assets:
            self.asset_list.addItem(i)

    def onAssetChanged(self):
        self.version_list.clear()
        if not self.shot_index:
            return

        asset = self.selectedAsset()
        version = self.shot_index[asset]["versions"]
        for i in version:
            self.version_list.addItem(i)

    def onVersionChanged(self):
        self.component_list.clear()

        if not self.shot_index:
            return

        asset = self.selectedAsset()

        version = self.selectedVersion()

        components = self.shot_index[asset]["versions"][version]["components"]
        for i in components:
            self.component_list.addItem(i)

        description = self.shot_index[asset]["versions"][version]["description"]
        self.description_box.setPlainText(description)

    def onComponentChanged(self):
        if not self.component_list.selectedItems():
            self.load_button.setEnabled(False)
            return
        self.load_button.setEnabled(True)

    def onLoad(self):

        node = self.node
        project = self.selectedProject()
        sequence = self.selectedSequence()
        shot = self.selectedShot()
        asset = self.selectedAsset()
        version = self.selectedVersion()
        version = "v{}".format((version).zfill(3))
        component = self.selectedComponent()
        context = "{}/{}/{}/{}/{}/{}".format(project,
                                             sequence, shot, asset, 
                                             version, component)
        node.setParms({"context": context})
        self.close()


dialog = None


def show(parent=None):
    global dialog
    dialog = ShotListDialog(parent=parent)
    dialog.show()
    return dialog


def show_houdini(node):
    import hou
    global dialog
    dialog = ShotListDialog(node=node, parent=hou.qt.mainWindow())
    dialog.show()
    return dialog


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = ShotListDialog()
    w.show()
    sys.exit(app.exec_())
