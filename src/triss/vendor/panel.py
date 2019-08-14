import hou
from hutil.Qt import QtWidgets, QtCore


class BaseScrollablePanelWidget(QtWidgets.QDialog):
    def __init__(self, title=None, parent=None):
        super(BaseScrollablePanelWidget, self).__init__(parent=parent)

        self.main_layout = QtWidgets.QVBoxLayout(self)

        if title:
            self.title = QtWidgets.QLabel('<b>%s</b>' % title)
            self.setWindowTitle(title)
        self.body_widget = QtWidgets.QWidget(self)
        self.body_layout = QtWidgets.QVBoxLayout(self.body_widget)
        self.body_layout.setSpacing(0)

        self.scroll = QtWidgets.QScrollArea(self)
        self.setStyle()
        self.scroll.setWidget(self.body_widget)
        self.scroll.setWidgetResizable(True)
        self.scroll.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.body_layout.setAlignment(QtCore.Qt.AlignTop)

        self.error_wid = QtWidgets.QWidget(self)
        self.error_lay = QtWidgets.QHBoxLayout(self.error_wid)
        self.error_lbl = QtWidgets.QLabel(
            'There are errors in your shitty code')
        self.error_lbl.setStyleSheet('color: red')
        self.error_btn = QtWidgets.QPushButton('x')
        self.error_btn.setMaximumWidth(25)
        self.error_btn.clicked.connect(self.error_wid.hide)
        self.error_lay.addWidget(self.error_lbl)
        self.error_lay.addWidget(self.error_btn)

        # if title:
            # self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.scroll)
        self.main_layout.addWidget(self.error_wid)

        self.error_wid.hide()

    def setStyle(self):
        self.setWindowIcon(hou.qt.mainWindow().windowIcon())
        self.setStyleSheet(hou.ui.qtStyleSheet())
