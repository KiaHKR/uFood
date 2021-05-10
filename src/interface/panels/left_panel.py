"""File for containing Components class."""
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from src.interface.styling import qss
import src.bin.logic as logic


class Components:
    """Components class that holds all widgets."""

    widgets = {}
    __object_names = (
        "search_bar",
        "search_btn",
        "search_btn_bg",
        "search_filter_btn",
        "search_filter_menu",
        "donate_btn",
        "donate_text",
        "filter_dropdown",
        "logo",
        "selected_items",
        "time_slider",
        "time_label",
    )
    path = "src/interface/assets/"

    def __init__(self):
        """Components class constructor."""
        self.widgets[self.__object_names[0]] = self.__search_bar()
        self.widgets[self.__object_names[1]] = self.__search_btn()
        self.widgets[self.__object_names[2]] = self.__search_icon_bg()
        self.widgets[self.__object_names[3]] = self.__search_filter_btn()
        self.widgets[self.__object_names[4]] = self.__search_filter_menu()
        self.widgets[self.__object_names[5]] = self.__donate_btn()
        self.widgets[self.__object_names[6]] = self.__donate_text()
        self.widgets[self.__object_names[7]] = self.__drop_down_results()
        self.widgets[self.__object_names[8]] = self.__logo()
        self.widgets[self.__object_names[9]] = self.__selected_items()
        self.widgets[self.__object_names[10]] = self.__time_slider()
        self.widgets[self.__object_names[11]] = self.__time_label()

    def __search_bar(self):
        """Search bar widget for ingredients."""
        search_bar = qtw.QLineEdit()
        search_bar.setObjectName("search_bar")
        search_bar.setFixedHeight(40)
        search_bar.setPlaceholderText("Search me... I'm dry ;)")
        search_bar.setStyleSheet("background-color: white; font-size: 14px;")
        return search_bar

    def __search_btn(self):
        """Button to begin searching for ingredients."""
        search_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self.path + "search.png"))
        )
        search_btn.setIconSize(qtc.QSize(25, 25))
        search_btn.setObjectName(self.__object_names[1])
        search_btn.setStyleSheet(
            """
            border: none;
            background-color: transparent;
            margin-top: 1px;
            position: absolute;
        """
        )
        search_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        return search_btn

    def __search_icon_bg(self):
        """Icon for search button."""
        search_btn_bg = qtw.QLabel()
        search_btn_bg.setStyleSheet(
            "background-color: white; margin-top: 1.1px;"
        )
        search_btn_bg.setFixedSize(
            30, self.widgets[self.__object_names[0]].height() - 1
        )
        search_btn_bg.setObjectName(self.__object_names[2])
        return search_btn_bg

    def __search_filter_btn(self):
        """Filter button for selecting diet type."""
        search_filter_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self.path + "filter_icon.png"))
        )
        search_filter_btn.setStyleSheet(
            "background-color: white; border: none;"
        )
        search_filter_btn.setObjectName("search_filter_btn")
        # search_filter_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        search_filter_btn.setFixedSize(
            30, self.widgets[self.__object_names[0]].height() - 2
        )
        search_filter_btn.setContentsMargins(5, 0, 0, 0)
        return search_filter_btn

    def __search_filter_menu(self):
        """Menu for selecting diet type."""
        menu = qtw.QMenu()
        menu.setContentsMargins(5, 0, 0, 0)
        act1 = qtw.QAction("Vegan", menu)
        act1.setCheckable(True)
        act1.setObjectName("Vegan")
        act2 = qtw.QAction("Vegetarian", menu)
        act2.setCheckable(True)
        act2.setObjectName("Vegetarian")
        act3 = qtw.QAction("Pescatarian", menu)
        act3.setCheckable(True)
        act3.setObjectName("Pescatarian")
        act4 = qtw.QAction("Keto", menu)
        act4.setCheckable(True)
        act4.setObjectName("Keto")
        act5 = qtw.QAction("Paleo", menu)
        act5.setCheckable(True)
        act5.setObjectName("Paleo")

        menu.addAction(act1)
        menu.addAction(act2)
        menu.addAction(act3)
        menu.addAction(act4)
        menu.addAction(act5)
        menu.setObjectName(self.__object_names[4])

        return menu

    def __donate_btn(self):
        """Donate label for facebook link."""
        donate_btn = qtw.QLabel(
            pixmap=qtg.QPixmap(self.path + "fb_icon.png").scaled(30, 30)
        )
        donate_btn.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        donate_btn.setObjectName(self.__object_names[5])
        return donate_btn

    def __donate_text(self):
        """Text for next to donate image."""
        donate_text = qtw.QLabel("DONATE FOOD")
        donate_text.setStyleSheet(
            """
            font-weight: bold;
            font-size: 18px;
            color: white;
        """
        )
        donate_text.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        donate_text.setObjectName(self.__object_names[6])
        return donate_text

    def __drop_down_results(self):
        """Drop down menu to show results of search bar."""
        drop_down_results = qtw.QListWidget()
        drop_down_results.setStyleSheet(
            qss.scrollbar()
            + """QListWidget{
                color: white;
                background-color: #1c1c1c;
                margin-left: 0px;
                font-size: 14px;
                border: none;
        }"""
        )
        drop_down_results.setVisible(False)
        drop_down_results.setMaximumWidth(300)
        drop_down_results.setMinimumWidth(150)
        drop_down_results.setMaximumHeight(200)
        drop_down_results.setObjectName(self.__object_names[7])
        return drop_down_results

    def __logo(self):
        """Label to hold the application logo."""
        logo = qtw.QLabel()
        logo.setObjectName(self.__object_names[8])
        logo.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return logo

    def __selected_items(self):
        """List widget to hold selected items."""
        list = qtw.QListWidget()
        list.setStyleSheet(
            qss.scrollbar()
            + """QListWidget{
                color: white;
                background-color: transparent;
                margin-top: 50px;
                margin-left: 0px;
                font-size: 14px;
                border: none;
        }"""
        )
        list.setVisible(False)
        list.setObjectName(self.__object_names[9])
        list.addItems(logic.selected_ingredients)
        return list

    def __time_slider(self):
        """Slider to filter recipes based on cooking time"""

        sl = qtw.QSlider(qtc.Qt.Horizontal)
        max_time = logic.Logic.max_cook_time()
        sl.setRange(0, max_time)
        sl.setValue(max_time)
        sl.setTickInterval(1)
        sl.setObjectName(self.__object_names[10])

        return sl

    def __time_label(self):
        max_time = logic.Logic.max_cook_time()
        label = qtw.QLabel(str(max_time))
        label.setAlignment(qtc.Qt.AlignCenter | qtc.Qt.AlignVCenter)
        label.setMinimumWidth(80)
        label.setStyleSheet("color: white;")
        label.setObjectName(self.__object_names[11])
        return label
