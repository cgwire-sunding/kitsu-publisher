from Qt import QtWidgets, QtCore, QtCompat


class PreviewWidget(QtWidgets.QWidget):
    def __init__(self, parent, preview_file):
        super(PreviewWidget, self).__init__(parent)
        self.parent = parent
        self.desired_geometry = parent.desired_geometry
        self.preview_file = preview_file
        self.setup_ui()
        self.complete_ui()
        self.manage_size()

    def setup_ui(self):
        QtCompat.loadUi("../resources/views/PreviewWidget.ui", self)
        self.preview_vertical_layout = self.findChild(
            QtWidgets.QVBoxLayout, "preview_vertical_layout"
        )
        self.toolbar_widget = self.findChild(
            QtWidgets.QWidget, "toolbar_widget"
        )
        self.annote_button = self.findChild(
            QtWidgets.QPushButton, "annote_button"
        )
        self.delete_button = self.findChild(
            QtWidgets.QPushButton, "delete_button"
        )
        self.download_button = self.findChild(
            QtWidgets.QPushButton, "download_button"
        )
        self.full_screen_button = self.findChild(
            QtWidgets.QPushButton, "full_screen_button"
        )

    def complete_ui(self):
        pass

    def manage_size(self):
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.setFixedWidth(self.desired_geometry.width())
        self.toolbar_widget.setFixedWidth(self.desired_geometry.width())
        self.setFixedHeight(self.get_height())

    def clear(self):
        self.preview_vertical_layout.removeWidget(self.annote_button)
        self.preview_vertical_layout.removeWidget(self.delete_button)
        self.preview_vertical_layout.removeWidget(self.download_button)
        self.preview_vertical_layout.removeWidget(self.full_screen_button)
        self.preview_vertical_layout.removeWidget(self.toolbar_widget)
        self.clear_setup_media_widget()
        self.deleteLater()

    def clear_setup_media_widget(self):
        pass