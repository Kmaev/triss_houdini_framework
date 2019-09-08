from __future__ import print_function
from Qt import QtWidgets, QtCore
from triss import _houdini
import os
reload(_houdini)


class SaveFileDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SaveFileDialog, self).__init__(parent=parent)
        self.resize(450, 100)

        self.central_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.central_layout)
        # self.central_layout.setSpacing(10)
        self.central_layout.setAlignment(QtCore.Qt.AlignTop)

        self.input_label = QtWidgets.QLabel("Type scene name to save")
        self.central_layout.addWidget(self.input_label)

        self.name_input = QtWidgets.QLineEdit()
        self.name_input.setPlaceholderText("my_nice_new_scene")
        self.central_layout.addWidget(self.name_input)

        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.central_layout.addItem(spacerItem1)

        self.output_label = QtWidgets.QLabel("Your scene will be saved here:")
        self.central_layout.addWidget(self.output_label)

        self.output_path = QtWidgets.QLineEdit()
        self.output_path.setReadOnly(True)
        # self.output_path.setDisabled(True)
        self.output_path.setObjectName('SaveDialogOutput')
        self.central_layout.addWidget(self.output_path)

        spacerItem2 = QtWidgets.QSpacerItem(
            40, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.central_layout.addItem(spacerItem2)
        self.save_button = QtWidgets.QPushButton("Save")
        self.central_layout.addWidget(self.save_button)

        self.name_input.textChanged.connect(self.getScenePathPreview)
        self.save_button.clicked.connect(self.saveScene)

        style_folder = os.environ.get("STYLE_TRISS")
        with open(os.path.join(style_folder, "style_hou.qss"), 'r') as f:
            style = f.read()
        self.setStyleSheet(style)

    def getScenePathPreview(self, text):
        self.scene_path = _houdini.makeScenePath(scene_name=text)
        self.output_path.setText(self.scene_path)

    def saveScene(self):
        print(self.scene_path)
        _houdini.saveScene(self.scene_path)
        self.close()


dialog = None


def show_houdini():
    import hou
    global dialog
    dialog = SaveFileDialog(parent=hou.qt.mainWindow())
    dialog.show()
    return dialog
