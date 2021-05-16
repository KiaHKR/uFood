"""Right_bottom_panel for containing components class."""
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import urllib.request as request
from src.bin import logic

from src.interface.styling import qss


class Components:
    """Components class holds all Widgets for right_bottom_panel."""

    widgets = {}
    __object_names = (
        "search_count",  # 0
        "thumbnail_img",  # 1
        "recipe_title",  # 2
        "diet_type",  # 3
        "total_time",  # 4
        "total_time_icon",  # 5
        "ingredients",  # 6
        "scroll_area",  # 7
        "save_btn",  # 8
        "export_btn",  # 9
        "recipe_view_img",  # 10
        "recipe_view_title",  # 11
        "recipe_view_ingredients",  # 12
        "recipe_view_steps",  # 13
        "recipe_view_exit",  # 14
    )
    path = "src/interface/assets/"

    def __init__(self):
        """Is constructor of the components class."""
        self.widgets[self.__object_names[0]] = self.__search_count()
        self.widgets[self.__object_names[5]] = self.__total_time_icon()
        self.widgets[self.__object_names[7]] = self.__scroll_area()
        # self.widgets[self.__object_names[8]] = self.__save_btn()
        self.widgets[self.__object_names[9]] = self.__export_btn()
        self.widgets[self.__object_names[10]] = self.__recipe_view_img()
        self.widgets[self.__object_names[11]] = self.__recipe_view_title()
        self.widgets[
            self.__object_names[12]
        ] = self.__recipe_view_ingredients()
        self.widgets[self.__object_names[13]] = self.__recipe_view_steps()
        self.widgets[self.__object_names[14]] = self.__recipe_view_exit()

    def __export_btn(self):
        """For the export button label."""
        export_btn = qtw.QLabel(
            pixmap=qtg.QPixmap(self.path + "download_icon.png").scaled(30, 30)
        )
        export_btn.setObjectName(self.__object_names[9])
        export_btn.setFixedSize(30, 30)
        export_btn.setStyleSheet("border : none;")
        export_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return export_btn

    def save_btn(self, id):
        """For the save button label."""
        id_list = logic.Sync().fav_list
        saved = False

        for i in id_list:
            if i == id:
                saved = True

        if saved is False:
            save_btn = qtw.QLabel(
                pixmap=qtg.QPixmap(self.path + "fav_icon_empty.png").scaled(
                    30, 30
                )
            )
        elif saved is True:
            save_btn = qtw.QLabel(
                pixmap=qtg.QPixmap(self.path + "fav_icon.png").scaled(30, 30)
            )

        save_btn.setObjectName(self.__object_names[8])
        save_btn.setFixedSize(30, 30)
        save_btn.setStyleSheet("border : none;")
        save_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return save_btn

    def __search_count(self):
        """For counting searches."""
        count = qtw.QLabel("0")
        count.setObjectName(self.__object_names[0])
        count.setStyleSheet(
            "color: #aeaeae; font-size: 14px; font-weight: bold;"
        )
        return count

    def thumbnail_img(self, path_thumbnail):
        """For label that hold the recipe thumbnail."""
        if path_thumbnail is None:
            img = qtw.QLabel(
                pixmap=qtg.QPixmap(self.path + "img_placeholder.png").scaled(
                    120, 120
                )
            )
        else:
            req = request.Request(
                path_thumbnail, headers={"User-Agent": "Mozilla/5.0"}
            )
            url = request.urlopen(req).read()
            pixmap = qtg.QPixmap()
            pixmap.loadFromData(url)
            pixmap.scaled(120, 120)
            img = qtw.QLabel()
            img.setPixmap(pixmap)

        # might need to change this
        img.setObjectName(self.__object_names[1])
        img.setFixedSize(132, 132)
        img.setStyleSheet("background-color: transparent;")
        img.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return img

    def recipe_title(self, name):
        """Label for recipe title."""
        title = qtw.QLabel(name)
        title.setStyleSheet(
            "color: white; font-size: 20px; font-weight: bold;"
        )
        title.setObjectName(self.__object_names[2])
        return title

    def diet_type(self, diet):
        """Label for diet type."""
        diet_type = qtw.QLabel(diet)
        if diet == "None":
            diet_colour = "transparent"
        elif diet == "Vegan":
            diet_colour = "#32a852"
        elif diet == "Vegetarian":
            diet_colour = "#137d2c"
        elif diet == "Keto":
            diet_colour = "#d18436"
        elif diet == "Paleo":
            diet_colour = "#336600"
        else:
            diet_colour = "#8c0000"  # remove later

        diet_type.setStyleSheet(
            f"color: {diet_colour}; font-size: 14px; font-weight: bold;"
        )
        diet_type.setObjectName(self.__object_names[3])
        return diet_type

    def total_time(self, time):
        """Label for cooking time."""
        total_time = qtw.QLabel(time)
        total_time.setStyleSheet(
            "color: white; font-size: 12px; font-weight: bold;"
        )
        total_time.setObjectName(self.__object_names[4])
        return total_time

    def __total_time_icon(self):
        """Label for timer icon."""
        total_time_icon = qtw.QLabel(
            pixmap=qtg.QPixmap(self.path + "timer2.png").scaled(30, 30)
        )
        total_time_icon.setFixedSize(35, 35)
        total_time_icon.setContentsMargins(0, 0, 0, 0)
        total_time_icon.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        total_time_icon.setObjectName(self.__object_names[5])

        return total_time_icon

    def ingredients(self, ingr):
        """Label for recipe ingredients."""
        ingredients = qtw.QLabel(ingr)
        ingredients.setStyleSheet(
            "color: white; font-size: 14px; font-style: italic;"
        )
        ingredients.setObjectName(self.__object_names[6])
        return ingredients

    def __scroll_area(self):
        """Scroll area for all the recipe cards."""
        scroll_area = qtw.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(qss.scrollbar())
        scroll_area.setFrameShape(qtw.QFrame.Shape.NoFrame)
        scroll_area.setObjectName(self.__object_names[7])

        result_box = qtw.QWidget()
        result_box.setLayout(qtw.QVBoxLayout())
        result_box.setObjectName("result_box")
        result_box.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignTop)
        result_box.setMinimumWidth(725)

        scroll_area.setWidget(result_box)

        return scroll_area

    def __recipe_view_img(self):
        """Recipe view img."""
        img = qtw.QLabel(
            pixmap=qtg.QPixmap(self.path + "img_placeholder.png").scaled(
                120, 120
            )
        )
        img.setObjectName(self.__object_names[10])
        img.setFixedSize(132, 132)
        img.setStyleSheet("background-color: transparent;")
        img.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return img

    def __recipe_view_title(self):
        """Recipe view title."""
        title = qtw.QLabel("PLACEHOLDER TITLE")
        title.setStyleSheet(
            "color: white; font-size: 48px; font-weight: bold;"
        )
        title.setWordWrap(True)
        title.setObjectName(self.__object_names[11])
        return title

    def __recipe_view_ingredients(self):
        """Recipe view ingredients."""
        ingredients = qtw.QLabel()
        ingredients.setText("Cake\nCookies")
        ingredients.setStyleSheet("color: white; font-size: 14px;")
        ingredients.setObjectName(self.__object_names[12])
        ingredients.setAlignment(qtc.Qt.AlignmentFlag.AlignTop)
        return ingredients

    def __recipe_view_steps(self):
        """Recipe view steps."""
        steps = qtw.QLabel()
        steps.setText("STEP 1 \nSTEP 2")
        steps.setStyleSheet("color: white; font-size: 14px;")
        steps.setWordWrap(True)
        steps.setAlignment(qtc.Qt.AlignmentFlag.AlignLeft)
        steps.setObjectName(self.__object_names[13])
        return steps

    def __recipe_view_exit(self):
        """Push button for exiting recipe view."""
        fav_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self.path + "back_icon.png"))
        )
        fav_btn.setIconSize(qtc.QSize(15, 15))
        fav_btn.setObjectName(self.__object_names[14])
        fav_btn.setStyleSheet("border: none;")
        fav_btn.setFixedWidth(35)
        fav_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return fav_btn
