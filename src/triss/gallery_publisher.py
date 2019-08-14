from __future__ import print_function
from triss.vendor.Qt import QtWidgets, QtCore, QtGui
from triss.vendor import flow_layout
from triss import _houdini
from triss import res
import hou
# Houdini helper module
import stateutils
import os
reload(_houdini)


class PublishDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(PublishDialog, self).__init__(parent=parent)

        self.central_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.central_layout)

        self.resize(400, 600)
        self.setWindowTitle('Gallery Publisher v0.1.6')
        self.setObjectName('Gallery_Publisher')

        self.gallery_grp = QtWidgets.QGroupBox('Available Galleries')
        self.gallery_list = QtWidgets.QListWidget(self)
        self.gallery_list.setAlternatingRowColors(True)
        self.gallery_layout = QtWidgets.QVBoxLayout()
        self.gallery_grp.setLayout(self.gallery_layout)
        self.gallery_layout.addWidget(self.gallery_list)
        self.gallery_layout.setContentsMargins(0, 5, 0, 5)

        self.addGalleries()
        self.gallery = None
        self.preview_file = None

        self.settings_grp = QtWidgets.QGroupBox('Export settings')
        self.settings_layout = QtWidgets.QVBoxLayout(self.settings_grp)
        # self.settings_layout.setSpacing(0)
        self.settings_layout.setContentsMargins(0, 5, 0, 5)

        self.group_name = QtWidgets.QLineEdit()
        self.group_name.setPlaceholderText("Write group name here")
        self.description = QtWidgets.QTextEdit()
        self.description.setPlaceholderText("Write description here")

        self.do_flipbook = QtWidgets.QCheckBox('Add Flipbook')
        self.start_frame = QtWidgets.QSpinBox()
        self.end_frame = QtWidgets.QSpinBox()
        self.start_frame.setDisabled(True)
        self.end_frame.setDisabled(True)
        self.start_frame.setRange(-99999999, 99999999)
        self.end_frame.setRange(-99999999, 99999999)
        self.start_frame.setValue(int(hou.expandString('$FSTART')))
        self.end_frame.setValue(int(hou.expandString('$FEND')))

        self.flipbook_layout = QtWidgets.QHBoxLayout()
        self.flipbook_layout.addWidget(self.do_flipbook)
        self.flipbook_layout.addWidget(self.start_frame)
        self.flipbook_layout.addWidget(self.end_frame)

        self.settings_layout.addWidget(self.group_name)
        self.settings_layout.addWidget(self.description)
        self.settings_layout.addLayout(self.flipbook_layout)

        self.publish_button = QtWidgets.QPushButton('Publish')

        self.central_layout.addWidget(self.gallery_grp)
        self.central_layout.addWidget(self.settings_grp)
        self.central_layout.addWidget(self.publish_button)

        self.gallery_list.itemSelectionChanged.connect(self.onGalleryChanged)
        self.publish_button.clicked.connect(self.publish)

        self.do_flipbook.toggled.connect(self.start_frame.setEnabled)
        self.do_flipbook.toggled.connect(self.end_frame.setEnabled)

        with open(r'E:\code\learn\resources\style.qss', 'r') as f:
            self.setStyleSheet(f.read())

    def addGalleries(self):
        gallery_list = ['shaders', 'sop_presets']
        [self.gallery_list.addItem(x) for x in gallery_list]

    def onGalleryChanged(self):
        selected = self.gallery_list.selectedItems()
        self.gallery = selected[0].text() if selected else None
        print(self.gallery)

    def doFlipbook(self):
        # Get the "Scene View" panel

        scene = stateutils.findSceneViewer()

        # Get a copy of the flipbook options
        flipbook_settings = scene.flipbookSettings().stash()
        flipbook_settings.frameRange((1, 10))
        preview_file = _houdini.getPreviewPath(
            self.gallery, self.group_name.text())
        preview_folder = os.path.dirname(preview_file)
        if not os.path.isdir(preview_folder):
            os.makedirs(preview_folder)
        flipbook_settings.output(preview_file)
        flipbook_settings.outputToMPlay(False)
        flipbook_settings.resolution((500, 500))
        flipbook_settings.useResolution(True)

        scene.flipbook(scene.curViewport(), flipbook_settings)

        publish_folder = os.path.dirname(
            _houdini.getMetadataFile(self.gallery, self.group_name.text()))
        self.preview_file = os.path.relpath(preview_file, publish_folder)

    def publish(self):
        nodes = hou.selectedNodes()

        if self.gallery is not None and self.group_name.text():
            if self.do_flipbook.isChecked():
                self.doFlipbook()
            _houdini.save_nodes(gallery=self.gallery,
                                name=self.group_name.text(),
                                nodes=nodes,
                                description=self.description.toPlainText(),
                                preview=self.preview_file)
            self.close()


dialog = None


def show_houdini():
    import hou
    global dialog
    dialog = PublishDialog(parent=hou.qt.mainWindow())
    dialog.show()
    return dialog
