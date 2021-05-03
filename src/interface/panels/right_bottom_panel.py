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
    path = "src/interface/assets/"

    def __init__(self):
        self.widgets[self.__object_names[0]] = self.__search_count()
        self.widgets[self.__object_names[5]] = self.__total_time_icon()
        self.widgets[self.__object_names[7]] = self.__scroll_area()

    def __search_count(self):
        count = qtw.QLabel("0")
        count.setObjectName(self.__object_names[0])
        count.setStyleSheet(
            "color: #aeaeae; font-size: 14px; font-weight: bold;"
        )
        return count

    def thumbnail_img(self, path_thumbnail):
        # might need to change this
        img = qtw.QLabel(pixmap=qtg.QPixmap(path_thumbnail).scaled(120, 120))
        img.setObjectName(self.__object_names[1])
        img.setFixedSize(135, 135)
        img.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return img

    def recipe_title(self, name):
        title = qtw.QLabel(name)
        title.setObjectName(self.__object_names[2])
        return title

    def diet_type(self, diet):
        diet_type = qtw.QLabel(diet)
        diet_type.setObjectName(self.__object_names[3])
        return diet_type

    def total_time(self, time):
        total_time = qtw.QLabel(time)
        total_time.setObjectName(self.__object_names[4])
        return total_time

    def __total_time_icon(self):
        total_time_icon = qtw.QLabel(
            pixmap=qtg.QPixmap(self.path + "timer2.png").scaled(30, 30)
        )
        total_time_icon.setFixedSize(35, 35)
        total_time_icon.setContentsMargins(0, 0, 0, 0)
        total_time_icon.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        total_time_icon.setObjectName(self.__object_names[5])

        return total_time_icon

    def ingredients(self, ingr):
        ingredients = qtw.QLabel(ingr)
        ingredients.setObjectName(self.__object_names[6])
        return ingredients

    def __scroll_area(self):
        scroll_area = qtw.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(qss.scrollbar())
        scroll_area.setObjectName(self.__object_names[7])
        return scroll_area