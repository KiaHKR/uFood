from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from src.interface.styling import qss


class Components:
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
    )
    _path = "src/interface/assets/"

    def __init__(self):
        self.widgets[self.__object_names[0]] = self.__search_bar()
        self.widgets[self.__object_names[1]] = self.__search_btn()
        self.widgets[self.__object_names[2]] = self.__search_icon_bg()
        self.widgets[self.__object_names[3]] = self.__search_filter_btn()
        self.widgets[self.__object_names[4]] = self.__search_filter_menu()
        self.widgets[self.__object_names[5]] = self.__donate_btn()
        self.widgets[self.__object_names[6]] = self.__donate_text()
        self.widgets[self.__object_names[7]] = self.__drop_down_results()
        self.widgets[self.__object_names[8]] = self.__logo()

    def __search_bar(self):
        search_bar = qtw.QLineEdit()
        search_bar.setObjectName("search_bar")
        search_bar.setFixedHeight(40)
        search_bar.setPlaceholderText("Search me... I'm dry ;)")
        search_bar.setStyleSheet("background-color: white; font-size: 14px;")
        # set connections
        # set QSS
        return search_bar

    def __search_btn(self):
        search_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self._path + "search.png"))
        )
        search_btn.setIconSize(qtc.QSize(25, 25))
        search_btn.setObjectName(self.__object_names[1])
        # set connection
        search_btn.setStyleSheet(
            """
            border: none;
            background-color: transparent;
            margin-top: 1px;
            position: absolute;
        """
        )
        return search_btn

    def __search_icon_bg(self):
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
        search_filter_btn = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap(self._path + "filter_icon.png"))
        )
        search_filter_btn.setStyleSheet("background-color: white;")
        search_filter_btn.setObjectName("search_filter_btn")
        search_filter_btn.setFixedSize(
            30, self.widgets[self.__object_names[0]].height() - 1
        )
        search_filter_btn.setContentsMargins(5, 0, 0, 0)
        return search_filter_btn

    def __search_filter_menu(self):
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
        donate_btn = qtw.QLabel(
            pixmap=qtg.QPixmap(self._path + "fb_icon.png").scaled(30, 30)
        )
        donate_btn.setObjectName(self.__object_names[5])
        return donate_btn

    def __donate_text(self):
        donate_text = qtw.QLabel("DONATE")
        donate_text.setStyleSheet(
            """
            font-weight: bold;
            font-size: 18px;
            color: white;
        """
        )
        donate_text.setObjectName(self.__object_names[6])
        return donate_text

    def __drop_down_results(self):
        drop_down_results = qtw.QListWidget()
        drop_down_results.setStyleSheet(
            qss.scrollbar()
            + """QListWidget{
                background-color: white;
                margin-left: 20px;
                font-size: 14px;
        }"""
        )
        drop_down_results.setObjectName(self.__object_names[7])
        return drop_down_results

    def __logo(self):
        logo = qtw.QLabel()
        logo.setObjectName(self.__object_names[8])
        logo.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        return logo
