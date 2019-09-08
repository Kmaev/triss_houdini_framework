from __future__ import print_function
from Qt import QtWidgets, QtCore
from triss import _houdini
import os
import hou


class OpenFileDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(OpenFileDialog, self).__init__(parent=parent)
        self.setObjectName('OpenDialog')
        self.resize(400, 300)

        self.central_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.central_layout)

        self.root_label = QtWidgets.QLabel("Root:")

        self.user_data = _houdini.OpenFile()
        self.tree_widget = QtWidgets.QTreeWidget(self)
        self.tree_widget.setHeaderLabels([self.user_data.user_folder])

        self.load_button = QtWidgets.QPushButton("Load")

        self.central_layout.addWidget(self.root_label)
        self.central_layout.addWidget(self.tree_widget)
        self.central_layout.addWidget(self.load_button)

        self.populateTree()

        self.load_button.clicked.connect(self.onLoad)
        self.tree_widget.itemDoubleClicked.connect(self.onLoad)

        style_folder = os.environ.get("STYLE_TRISS")
        with open(os.path.join(style_folder, "style_hou.qss"), 'r') as f:
            style = f.read()
        self.setStyleSheet(style)

    def populateTree(self):
        root = self.tree_widget.invisibleRootItem()

        for task_folder in self.user_data.user_tasks.keys():
            task = QtWidgets.QTreeWidgetItem(root)
            task.setText(0, task_folder)
            scene_folder = os.path.join(
                self.user_data.user_folder, task_folder)

            if os.path.isdir(scene_folder):
                scene_list = os.listdir(scene_folder)
                for hip_file in scene_list:
                    if hip_file.endswith(".hip"):
                        scene_path = os.path.join(scene_folder, hip_file)
                        scene_path = os.path.normpath(scene_path)
                        scene_path = scene_path.replace('\\', '/')
                        scene = QtWidgets.QTreeWidgetItem(task)
                        scene.setData(0, QtCore.Qt.UserRole, scene_path)
                        scene.setText(0, hip_file)

    def onLoad(self):
        item = self.tree_widget.selectedItems()[0]
        scene_path = item.data(0, QtCore.Qt.UserRole)
        hou.hipFile.load(scene_path)
        self.close()


dialog = None


def show_houdini():
    import hou
    global dialog
    dialog = OpenFileDialog(parent=hou.qt.mainWindow())
    dialog.show()
    return dialog
