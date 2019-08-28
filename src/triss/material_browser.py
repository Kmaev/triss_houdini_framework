from __future__ import print_function
from Qt import QtWidgets, QtCore, QtGui
import clique
import flow_layout
from triss import _houdini
import json
import hou
import os
from triss import res

reload(_houdini)

NOPREVIEW_PATH = os.path.join(os.environ.get(
    "STYLE_TRISS"), "images/no-thumb.png")
out = os.environ.get("OUT")


class MaterialListDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MaterialListDialog, self).__init__(parent=parent)

        self.resize(850, 600)
        # self.resize(0,0)
        self.setWindowTitle('Material Browser v0.1.6')

        # Variable initialization

        self.gallery = 'shaders'
        self.material_labels = []

        # CENTRAL layout
        self.central_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.central_layout)
        self.central_layout.setContentsMargins(7, 7, 7, 7)

        self.title_layout = QtWidgets.QVBoxLayout()
        self.title_layout.setContentsMargins(0, 0, 1, 0)
        self.title_groups = QtWidgets.QLabel(
            'Shader groups available to import')
        self.title_layout.addWidget(self.title_groups)

        self.gallery_combo = QtWidgets.QComboBox()

        gallery_list = ['shaders', 'sop_presets']

        for i in gallery_list:
            self.gallery_combo.addItem(i, i)
        self.gallery_combo.currentIndexChanged.connect(self.onGalleryChanged)

        self.title_layout.addWidget(self.gallery_combo)

        self.central_layout.addLayout(self.title_layout)

        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splitter.setContentsMargins(10, 10, 10, 10)

        self.central_layout.addWidget(self.splitter)

        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # FLOW layout
        self.flow_widget = QtWidgets.QWidget()
        self.flow_layout = flow_layout.FlowLayout()
        self.flow_layout.setSpacing(10)
        self.flow_widget.setLayout(self.flow_layout)
        self.scroll_area.setWidget(self.flow_widget)
        self.splitter.addWidget(self.scroll_area)

        # DISPLAY WIDGET layout , right side
        self.display_widget = DisplayWidget()
        self.splitter.addWidget(self.display_widget)

        self.splitter.setSizes([300, 300])

        self.load_button = QtWidgets.QPushButton('Load selected')
        self.central_layout.addWidget(self.load_button)

        self.load_button.clicked.connect(self.onLoad)
        style_folder = os.environ.get("STYLE_TRISS")
        with open(os.path.join(style_folder, "style_hou.qss"), 'r') as f:
            style = f.read()

        self.setStyleSheet(style)
        self.display_widget.style = style

        if self.parent():
            self.parent().setStyleSheet(self.parent().styleSheet())

        self.onGalleryChanged(0)

    def onGalleryChanged(self, index):
        sel = self.gallery_combo.itemData(index)
        self.gallery = sel
        self.populateMaterialLabels(gallery=sel)
        self.display_widget.current_combo.clear()
        self.display_widget.selection = []

        self.display_widget.setCompleterForGallery(self.gallery)
        self.display_widget.parent_edit.setText('')
        self.display_widget.setCurrent(None)

    def populateMaterialLabels(self, gallery):
        while self.flow_layout.count() > 0:
            item = self.flow_layout.takeAt(0)
            if not item:
                continue

            w = item.widget()
            if w:
                w.deleteLater()

        for shader_folder in os.listdir(os.path.join(out, gallery)):
            new_widget = MaterialLabel(gallery=gallery,
                                       shader_name=shader_folder)
            new_widget.onSelected.connect(self.onLabelSelected)

            self.material_labels.append(new_widget)
            self.flow_layout.addWidget(new_widget)

    def onLoad(self):

        for widget in self.material_labels:
            if widget.selected:
                if widget.metadata['group_name'] in self.display_widget.checks.keys():
                    elements = self.display_widget.checks[widget.metadata['group_name']]
                    _elements = []
                    for key, value in elements.items():
                        if value is True:
                            _elements.append(key)
                    parent = hou.node(self.display_widget.parent_edit.text())
                    if parent is None:
                        if self.gallery == "shaders":
                            parent = hou.node("/shop")
                        elif not parent:

                            message = ('Must specify a parent for '
                                       'non-shader presets')
                            QtWidgets.QMessageBox.critical(
                                self, 'Error', message,)
                            raise RuntimeError(message)
                    else:
                        _houdini.load_nodes(
                            gallery=self.gallery,
                            name=widget.label.text(),
                            parent=parent,
                            elements=_elements
                        )

        return

    def onLabelSelected(self, matlabelwidget):
        self.display_widget.onSelectionChanged(matlabelwidget=matlabelwidget)
        # if selected.selected is True:
        #     self.display_widget.setCurrent(selected)


class DisplayWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(DisplayWidget, self).__init__(parent=parent)
        self.selection = []
        self.setObjectName('DisplayWidget')
        self.central_layout = QtWidgets.QVBoxLayout(self)

        self.checks = {}
        self.current_fb_frame = 0
        self.current = None
        self.style = ''

        self.thumb_label = QtWidgets.QLabel()
        self.seq_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.seq_slider.setVisible(False)
        self.items_list = QtWidgets.QLabel(" Selected items list")
        self.current_combo = QtWidgets.QComboBox()
        self.item_selection = QtWidgets.QLabel(" Elements list")
        self.item_selection_combo = QtWidgets.QComboBox()
        self.info_edit = QtWidgets.QTextEdit()
        self.info_edit.setReadOnly(True)

        # ESTO ES DE SALVA
        self.parent_edit = QtWidgets.QLineEdit()
        self.parent_edit.setPlaceholderText(
            "Write parent node here: '/obj/my_geometry'")

        # A PARTIR DE AQUI NO ES DE SALVA

        self.central_layout.addWidget(self.thumb_label)

        self.central_layout.addWidget(self.seq_slider)
        self.central_layout.addWidget(self.parent_edit)
        # self.central_layout.addWidget(self.items_list)
        self.central_layout.addWidget(self.current_combo)
        self.central_layout.addWidget(self.info_edit)
        self.central_layout.addWidget(self.item_selection)
        self.check_box_layout = QtWidgets.QVBoxLayout()
        self.central_layout.addLayout(self.check_box_layout)
        # self.central_layout.addWidget(self.item_selection_combo)

        self.central_layout.setAlignment(self.thumb_label,
                                         QtCore.Qt.AlignCenter)

        self.current_combo.currentIndexChanged.connect(self.onComboChanged)
        self.seq_slider.valueChanged[int].connect(self.onSliderValueChanged)

        self.setCurrent(None)

    def setCompleterForGallery(self, gallery):
        if gallery == "shaders":
            allowed = ('shopnet', 'shop')
        if gallery == "sop_presets":
            allowed = ('subnet', 'geo')

        nodes = sorted([x.path() for x in hou.node('/').recursiveGlob('*')
                        if x.type().name() in allowed])

        completer = QtWidgets.QCompleter(list(nodes))
        completer.popup().setObjectName('completer')
        completer.popup().setStyleSheet(self.style)
        self.parent_edit.setCompleter(completer)

    def onSliderValueChanged(self, value):
        self.current_fb_frame = value

        preview = self.current.metadata['preview']
        preview = os.path.normpath(preview)
        preview = preview.replace('\\', '/')
        preview_folder = os.path.dirname(preview)

        img_list = os.listdir(preview_folder)
        collections, remainder = clique.assemble(img_list, minimum_items=1)
        if collections:
            thumb = list(collections[0])[self.current_fb_frame]
            if thumb:
                preview_path = os.path.join(preview_folder, thumb)
                pixmap = QtGui.QPixmap(preview_path)

                slider_len = len(list(collections[0]))
                try:
                    self.seq_slider.setMaximum(slider_len - 1)

                except IndexError as e:
                    raise RuntimeError("list index out of range")
            else:
                pixmap = QtGui.QPixmap(self.current.metadata['preview'])

        if not pixmap or pixmap.isNull():
            pixmap = QtGui.QPixmap(NOPREVIEW_PATH)

        size = QtCore.QSize(256, 256)
        pixmap = pixmap.scaled(size,
                               QtCore.Qt.KeepAspectRatioByExpanding,
                               QtCore.Qt.SmoothTransformation)

        self.thumb_label.setPixmap(pixmap)

    def onComboChanged(self, index):
        sel = self.current_combo.itemData(index)
        self.setCurrent(sel)
        self.populateItemSelectionCombo(index)

    def onSelectionChanged(self, matlabelwidget):
        if matlabelwidget.selected:
            if matlabelwidget not in self.selection:
                self.selection.append(matlabelwidget)
        else:
            if matlabelwidget in self.selection:
                self.selection.pop(self.selection.index(matlabelwidget))

        self.populateCombo()

        if matlabelwidget.selected:
            self.current_combo.setCurrentIndex(
                self.selection.index(matlabelwidget))

    def populateCombo(self):
        self.current_combo.clear()

        for matlabelwidget in self.selection:
            self.current_combo.addItem(matlabelwidget.metadata['group_name'],
                                       matlabelwidget)

    def populateItemSelectionCombo(self, index):
        while self.check_box_layout.count() > 0:
            item = self.check_box_layout.takeAt(0)
            if not item:
                continue

            w = item.widget()
            if w:
                w.deleteLater()

        matlabelwid = self.current_combo.itemData(index)
        if not matlabelwid:
            return

        deferred = {}

        for tag in ['all'] + matlabelwid.metadata['tags']:
            group = matlabelwid.metadata['group_name']

            node_check_box = QtWidgets.QCheckBox(tag)
            node_check_box.setProperty('group', group)
            self.check_box_layout.addWidget(node_check_box)

            if tag == 'all':
                node_check_box.toggled.connect(self.onAllToggled)
            else:
                node_check_box.toggled.connect(self.onCheckToggled)

                value = self.checks.get(group, {}).get(tag, True)
                deferred[node_check_box] = value

        for check, val in deferred.items():
            check.setChecked(val)

        # self.item_selection_combo.addItem(i,i)

    def getCheckboxes(self):
        cbs = []
        for i in range(self.check_box_layout.count()):
            widget = self.check_box_layout.itemAt(i).widget()
            cbs.append(widget)
        return cbs

    def onCheckToggled(self, value):
        check = self.sender()
        group = check.property('group')
        is_checked = check.isChecked()
        tag = check.text()

        self.checks.setdefault(group, {})
        self.checks[group][tag] = is_checked

        all_cb = [x for x in self.getCheckboxes() if x.text() == 'all'][0]

        others = [x.isChecked() for x in self.getCheckboxes()
                  if x.text() != 'all']

        all_cb.blockSignals(True)
        all_cb.setChecked(all(others))
        all_cb.blockSignals(False)

    def onAllToggled(self, value):
        for widget in self.getCheckboxes():
            if widget.text() == 'all':
                continue

            widget.setChecked(value)

    def setCurrent(self, matlabelwidget):
        self.current = matlabelwidget

        if matlabelwidget is None:
            pixmap = None
            text = ''
            self.seq_slider.setVisible(False)

        else:
            text = [
                'Description: {}'.format(
                    matlabelwidget.metadata['description']),
                'Elements: {}'.format(
                    ', '.join(matlabelwidget.metadata['tags']))
            ]
            text = '\n'.join(text)

            pixmap = QtGui.QPixmap(matlabelwidget.metadata['preview'])
            if matlabelwidget.preview_available is not False:
                self.seq_slider.setVisible(True)
                self.seq_slider.setValue(0)
            else:
                self.seq_slider.setVisible(False)

        if not pixmap or pixmap.isNull():
            pixmap = QtGui.QPixmap(NOPREVIEW_PATH)
            self.seq_slider.setVisible(False)

        size = QtCore.QSize(256, 256)
        pixmap = pixmap.scaled(size,
                               QtCore.Qt.KeepAspectRatioByExpanding,
                               QtCore.Qt.SmoothTransformation)

        self.info_edit.setText(text)
        self.thumb_label.setPixmap(pixmap)


class MaterialLabel(QtWidgets.QFrame):
    onSelected = QtCore.Signal(object)

    def __init__(self, gallery, shader_name, parent=None):
        super(MaterialLabel, self).__init__(parent=parent)

        self.setObjectName('MaterialLabel')
        self.preview_available = False
        self.selected = False
        self.metadata_file = _houdini.getMetadataFile(gallery, shader_name)
        with open(self.metadata_file, "r") as read_file:
            self.metadata = json.load(read_file)

        self.metadata['preview'] = self.getPreview(gallery, shader_name)

        # CENTRAL layout
        self.central_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.central_layout)
        self.central_layout.setContentsMargins(2, 2, 2, 2)
        self.central_layout.setSpacing(0)

        # PIXMAP
        pixmap = QtGui.QPixmap(self.metadata['preview'])
        if pixmap.isNull():
            pixmap = QtGui.QPixmap(r'')

        size = QtCore.QSize(100, 100)
        pixmap = pixmap.scaled(size,
                               QtCore.Qt.KeepAspectRatioByExpanding,
                               QtCore.Qt.SmoothTransformation)

        self.image_label = QtWidgets.QLabel()
        self.image_label.setPixmap(pixmap)
        self.image_label.setMaximumSize(size)
        self.image_label.setMinimumSize(size)

        # LABEL
        self.label = QtWidgets.QLabel()
        self.label.setText(shader_name)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # CENTRAL assignments
        self.central_layout.addWidget(self.image_label)
        self.central_layout.addWidget(self.label)

        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.image_label.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        # print('Click', self.label.text())

        if self.selected:
            self.setSelected(False)
        else:
            self.setSelected(True)

        self.onSelected.emit(self)

    def setSelected(self, value):
        self.selected = value
        self.setProperty('selected', value)
        self.setStyleSheet(self.styleSheet())

    def getPreview(self, gallery, shader_name):

        folder = os.path.dirname(self.metadata_file)

        preview = os.path.join(folder, "preview")

        if not os.path.isdir(preview):
            image_path = NOPREVIEW_PATH
            self.preview_available = False
        else:
            img_list = os.listdir(preview)
            collections, remainder = clique.assemble(img_list, minimum_items=1)
            self.preview_available = True
            thumb = None

            if collections:
                thumb = list(collections[0])[0]

            if not thumb and remainder:
                thumb = remainder[0]

            if thumb:
                # image_path = os.path.join(preview, img_list[0])
                image_path = os.path.join(preview, thumb)
            else:
                image_path = None

        return image_path


dialog = None


def show_houdini():
    import hou
    global dialog
    dialog = MaterialListDialog(parent=hou.qt.mainWindow())
    dialog.show()
    return dialog
