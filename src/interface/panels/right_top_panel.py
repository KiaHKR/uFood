"""Right_top_panel file for components class."""
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class Compontents:
    """Components class holds all widgets for right top panel."""

    widgets = {}
    __object_names = ("back_btn", "win_text", "fav_btn", "recipes_btn")
    __path = "src/interface/assets/"

    def __init__(self):
        """Is constructor for components class."""
        self.widgets[self.__object_names[0]] = self.__back_btn()
        self.widgets[self.__object_names[1]] = self.__win_text()
        self.widgets[self.__object_names[2]] = self.__fav_btn()
        self.widgets[self.__object_names[3]] = self.__recipes_btn()

    def __win_text(self):
        """For for top panel label."""
        win_text = qtw.QLabel("[ TEXT ]")
        win_text.setObjectName("win_text")
        win_text.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: white;"
        )
        win_text.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return win_text

    def __back_btn(self):
        """Back botton of the top panel."""
        back_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self.__path + "back_icon.png"))
        )
        back_btn.setIconSize(qtc.QSize(30, 30))
        back_btn.setObjectName(self.__object_names[0])
        back_btn.setStyleSheet("border: none;")
        back_btn.setFixedWidth(35)
        back_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return back_btn

    def __fav_btn(self):
        """Push button for favorites."""
        fav_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self.__path + "fav_icon.png"))
        )
        fav_btn.setIconSize(qtc.QSize(30, 30))
        fav_btn.setObjectName(self.__object_names[1])
        fav_btn.setStyleSheet("border: none;")
        fav_btn.setFixedWidth(35)
        fav_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return fav_btn

    def __recipes_btn(self):
        """Push button for trending recipes."""
        recipes_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self.__path + "recipes_icon.png"))
        )
        recipes_btn.setIconSize(qtc.QSize(30, 30))
        recipes_btn.setObjectName(self.__object_names[2])
        recipes_btn.setStyleSheet("border: none;")
        recipes_btn.setFixedWidth(35)
        recipes_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return recipes_btn
