"""Right_top_panel file for components class."""
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import src.interface.controller as controller


class Components:
    """Components class holds all widgets for right top panel."""

    widgets = {}
    __object_names = (
        "settings_btn",
        "win_text",
        "fav_btn",
        "recipes_btn",
        "trending_btn",
    )
    __path = "src/interface/assets/"

    def __init__(self):
        """Is constructor for components class."""
        self.widgets[self.__object_names[0]] = self.__settings_btn()
        self.widgets[self.__object_names[1]] = self.__win_text()
        self.widgets[self.__object_names[2]] = self.__fav_btn()
        self.widgets[self.__object_names[3]] = self.__recipes_btn()
        self.widgets[self.__object_names[4]] = self.__trending_btn()

    def __win_text(self):
        """For for top panel label."""
        win_text = qtw.QLabel("[ TEXT ]")
        win_text.setObjectName("win_text")
        win_text.setStyleSheet(
            "font-size: 18px; font-weight: bold; color: white;"
        )
        win_text.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return win_text

    def __settings_btn(self):
        """Back botton of the top panel."""
        settings_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self.__path + "settings_icon.png"))
        )
        settings_btn.setIconSize(qtc.QSize(30, 30))
        settings_btn.setObjectName(self.__object_names[0])
        settings_btn.setStyleSheet("border: none;")
        settings_btn.setFixedWidth(35)
        settings_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return settings_btn

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
        fav_btn.clicked.connect(
            lambda: controller.Controller.build_favorites()
        )
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

    def __trending_btn(self):
        """Back botton of the top panel."""
        trending_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self.__path + "trending_icon4.png"))
        )
        trending_btn.setIconSize(qtc.QSize(30, 30))
        trending_btn.setObjectName(self.__object_names[0])
        trending_btn.setStyleSheet("border: none;")
        trending_btn.setFixedWidth(35)
        trending_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return trending_btn
