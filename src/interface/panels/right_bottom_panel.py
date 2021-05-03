from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from src.interface.styling import qss


class Components:
    widgets = {}
    __object_names = (
        "search_count",
        "thumbnail_img",
        "recipe_title",
        "diet_type",
        "total_time",
        "total_time_icon",
        "ingredients",
        "scroll_area",
    )
    __path = "src/interface/assets"

    def __init__(self):
        self.widgets[self.__object_names[0]] = self.__search_count()
        self.widgets[self.__object_names[1]] = self.__thumbnail_img()
        self.widgets[self.__object_names[2]] = self.__recipe_title()
        self.widgets[self.__object_names[3]] = self.__diet_type()
        self.widgets[self.__object_names[4]] = self.__total_time()
        self.widgets[self.__object_names[5]] = self.__total_time_icon()
        self.widgets[self.__object_names[6]] = self.__ingredients()
        self.widgets[self.__object_names[7]] = self.__scroll_area()

    def __search_count(self):
        count = qtw.QLabel("0")
        count.setObjectName(self.__object_names[0])
        count.setStyleSheet(
            "color: #aeaeae; font-size: 14px; font-weight: bold;"
        )
        return count

    def __thumbnail_img(self):
        img = qtw.QLabel(
            pixmap=qtg.QPixmap(self.__path + "img_placeholder.png").scaled(
                120, 120
            )
        )
        img.setObjectName(self.__object_names[1])
        return img

    def __recipe_title(self):
        title = qtw.QLabel("[RECIPE NAME]")
        title.setObjectName(self.__object_names[2])
        return title

    def __diet_type(self):
        diet_type = qtw.QLabel("[DIET TYPE]")
        diet_type.setObjectName(self.__object_names[3])
        return diet_type

    def __total_time(self):
        total_time = qtw.QLabel("[TOTAL TIME]")
        total_time.setObjectName(self.__object_names[4])
        return total_time

    def __total_time_icon(self):
        total_time_icon = qtw.QLabel(
            pixmap=qtg.QPixmap(self.__path + "timer2.png")
        )
        total_time_icon.setObjectName(self.__object_names[5])
        return total_time_icon

    def __ingredients(self):
        ingredients = qtw.QLabel("[INGREDIENT LIST]")
        ingredients.setObjectName(self.__object_names[6])
        return ingredients

    def __scroll_area(self):
        scroll_area = qtw.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(qss.scrollbar())
        scroll_area.setObjectName(self.__object_names[7])
        return scroll_area