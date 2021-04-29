"""A class that stores prebuilt media widgets such as icons and images."""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

path = 'ui/assets/'


class MediaWidgets:
    """Allow for easier building with preset UI templates."""

    def create_imgWithScale(self, img_name, w, h):
        """Set and return an img at specified scale."""
        return qtw.QLabel(
            pixmap=qtg.QPixmap(path + img_name).scaled(w, h)
        )

    def create_img(self, img_name):
        """Set and return an img at default scale."""
        return qtw.QLabel(
                pixmap=qtg.QPixmap(path + img_name)
            )

    def create_pushIconWithSizes(self, icon_name, w, h):
        """Set and return a pushable icon at specified size."""
        return qtw.QPushButton(
                icon=qtg.QIcon(
                        qtg.QPixmap(path + icon_name))
                    ).setIconSize(qtc.QSize(w, h))

    def create_pushIcon(self, icon_name):
        """Set and return a pushable icon at default size."""
        return qtw.QPushButton(
                icon=qtg.QIcon(qtg.QPixmap(path + icon_name))
            )

    def create_iconWithSizes(self, icon_name, w, h):
        """Set and return an icon at specified size."""
        return qtg.QIcon(qtg.QPixmap(path + icon_name).size(qtc.QSize(w, h)))

    def create_icon(self, icon_name):
        """Set and return an icon at default size."""
        return qtg.QIcon(qtg.QPixmap(path + icon_name))

    def create_scrollArea(self):
        pass
