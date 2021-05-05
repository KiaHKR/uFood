import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from src.interface.panels.left_panel import Components as lcomp
from src.interface.panels.right_top_panel import Compontents as rtcomp
from src.interface.panels.right_bottom_panel import Components as rbcomp
from src.interface.styling import qss
from src.bin import logic

app = qtw.QApplication(os.sys.argv)
lpanel = lcomp().widgets
t_rpanel = rtcomp().widgets
b_rpanel = rbcomp().widgets


class Root(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # -- Build root panel
        layout = qtw.QHBoxLayout()
        self.screen = app.primaryScreen().size()
        self.resize(self.screen.width() // 2, self.screen.height() // 2)
        self.setStyleSheet("background-color: #1c1c1c;")
        self.setLayout(layout)


class View(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        root_view = Root()

        # left panel
        self.left_panel_widget = self.__left_panel_build()
        self.left_panel_widget.setMinimumWidth(300)
        root_view.layout().addWidget(self.left_panel_widget, 3)

        # right panel
        right_panel_widget = qtw.QWidget()
        right_panel_widget.setLayout(qtw.QVBoxLayout())

        # right top panel
        rtop_panel = self.__right_top_build()

        # right bottom panel
        info = self.__right_bottom_build()
        info.setMinimumWidth(725)

        b_rpanel["scroll_area"].setWidget(info)
        right_panel_widget.layout().addWidget(rtop_panel)

        right_panel_widget.layout().addWidget(b_rpanel["scroll_area"])
        right_panel_widget.setMinimumWidth(750)

        root_view.layout().addWidget(right_panel_widget, 7)

        self.qTimer = qtc.QTimer()
        self.qTimer.setInterval(1)
        self.qTimer.timeout.connect(
            lambda: Controller.update_logo_size(self.left_panel_widget)
        )
        self.qTimer.start()

        root_view.show()
        os.sys.exit(app.exec_())

    # !-- Left Panel

    def __left_panel_build(self):
        left_panel_widget = qtw.QWidget()
        left_panel_widget.setLayout(qtw.QVBoxLayout())
        Controller.update_logo_size(
            left_panel_widget
        )  # Grabbing logo size from window size
        left_panel_widget.layout().addWidget(lpanel["logo"])
        left_panel_widget.layout().addWidget(self.__search_widget_build())
        left_panel_widget.layout().addWidget(self.__donate_build())
        return left_panel_widget

    def __search_widget_build(self):
        """Build parent search widget."""
        search_widget = qtw.QWidget()
        search_widget.setLayout(qtw.QGridLayout())

        # Construct search button
        search_icon_widget = qtw.QWidget()
        search_icon_widget.setLayout(qtw.QStackedLayout())

        # Connect filter btn to filter menu
        lpanel["search_filter_btn"].setMenu(lpanel["search_filter_menu"])

        # Search bar on change connection
        lpanel["search_bar"].textChanged.connect(
            lambda: Controller.update_dropdown()
        )

        # filter_dropdown on select connection
        lpanel["filter_dropdown"].itemClicked.connect(
            lambda: Controller.select_ingredient(
                lpanel["filter_dropdown"].currentItem()
            )
        )

        # Add widgets to parent search layout
        search_widget.layout().addWidget(lpanel["search_bar"], 0, 0)
        search_widget.layout().addWidget(lpanel["filter_dropdown"], 1, 0)
        search_widget.layout().addWidget(lpanel["search_btn_bg"], 0, 2)
        search_widget.layout().addWidget(lpanel["search_btn"], 0, 2)
        search_widget.layout().addWidget(lpanel["search_filter_btn"], 0, 3)
        search_widget.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignTop)
        search_widget.layout().setSpacing(0)

        return search_widget

    def __save_build(self):
        """Build save feature."""
        save = qtw.QPushButton()
        save.setLayout(qtw.QHBoxLayout())
        save.layout().addWidget(b_rpanel["save_btn"])
        save.setStyleSheet(
            "border :2px solid ;"
            "border-top-color : #4f0005; "
            "border-left-color :#4f0005;"
            "border-right-color :#4f0005;"
            "border-bottom-color : #4f0005"
        )
        save.setFixedSize(50, 50)
        save.clicked.connect(lambda: Controller.save())
        return save

    def __export_build(self):
        """Build export feature."""
        export = qtw.QPushButton()
        export.setLayout(qtw.QHBoxLayout())
        export.setFixedSize(50, 50)
        # export.setStyleSheet("border: none;")
        export.setStyleSheet(
            "border :2px solid ;"
            "border-top-color : #f9f9f9; "
            "border-left-color :#f9f9f9;"
            "border-right-color :#f9f9f9;"
            "border-bottom-color : #f9f9f9"
        )
        export.layout().addWidget(b_rpanel["export_btn"])
        export.clicked.connect(lambda: Controller.export())
        return export

    def __donate_build(self):
        """Build donate feature."""
        donate = qtw.QPushButton()
        donate.setLayout(qtw.QHBoxLayout())
        donate.layout().addWidget(lpanel["donate_btn"], 0)
        donate.layout().addWidget(lpanel["donate_text"], 8)
        donate.setFixedSize(135, 50)
        donate.setStyleSheet("border: none;")
        donate.clicked.connect(lambda: Controller.donate_url())
        return donate

    # !-- Right Top Panel
    def __right_top_build(self):
        top_layout = qtw.QHBoxLayout()

        top_layout.addWidget(t_rpanel["back_btn"])
        top_layout.addWidget(t_rpanel["win_text"])
        top_layout.addWidget(t_rpanel["fav_btn"])
        top_layout.addWidget(t_rpanel["recipes_btn"])

        widget = qtw.QWidget()
        widget.setLayout(top_layout)
        return widget

    # !-- Right bottom panel
    def __right_bottom_build(self):
        bottom_layout = qtw.QWidget()
        # bottom_layout.setStyleSheet("border:2px solid green;")
        bottom_layout.setLayout(qtw.QVBoxLayout())
        bottom_layout.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignTop)

        # while there are results
        bottom_layout.layout().addWidget(self.__recipe_card())
        bottom_layout.layout().addWidget(self.__recipe_card())
        return bottom_layout

    def __recipe_card(
        self,
        name="[RECIPE NAME]",
        diet_type="[DIET TYPE]",
        total_time="[TOTAL TIME]",
        ingr="[INGREDIENT LIST]",
        pk_id="Error",
        thumbnail=rbcomp.path + "img_placeholder.png",
    ):
        recipe_card = qtw.QWidget()
        recipe_card.setLayout(qtw.QHBoxLayout())
        info = qtw.QWidget()
        info.setLayout(qtw.QVBoxLayout())
        info.layout().addWidget(rbcomp().recipe_title(name))
        info.layout().addWidget(rbcomp().diet_type(diet_type))

        time = qtw.QWidget()

        buttons = qtw.QWidget()
        buttons.setLayout(qtw.QVBoxLayout())
        buttons.layout().addWidget(self.__save_build())
        buttons.layout().addWidget(self.__export_build())
        buttons.layout().setSpacing(0)

        time.setLayout(qtw.QHBoxLayout())
        time.layout().addWidget(b_rpanel["total_time_icon"])
        time.layout().addWidget(rbcomp().total_time(total_time))
        time.layout().setContentsMargins(0, 0, 0, 0)
        time.layout().setSpacing(0)
        info.layout().addWidget(time)
        info.layout().addWidget(rbcomp().ingredients(ingr))
        info.layout().setContentsMargins(0, 0, 0, 0)
        info.layout().setSpacing(0)

        recipe_card.layout().addWidget(rbcomp().thumbnail_img(thumbnail), 1)
        recipe_card.layout().addWidget(info, 9)
        recipe_card.layout().addWidget(buttons, 1)

        recipe_card.setObjectName(pk_id)
        recipe_card.setFixedHeight(150)
        return recipe_card


class Controller:
    def update_logo_size(left_panel_widget):
        """Changes size of logo pixmap, based on parent panel size."""
        lpanel["logo"].setPixmap(
            qtg.QPixmap(lcomp.path + "logo_placeholder.png").scaled(
                left_panel_widget.width() // 1.9,
                left_panel_widget.height() // 2.5,
                qtc.Qt.AspectRatioMode.KeepAspectRatio,
            )
        )
        lpanel["logo"].setFixedHeight(left_panel_widget.height() // 2.5)

    def donate_url():
        os.startfile(
            "https://www.facebook.com/groups/1454991488172182/?notif_id=1620038256343772&notif_t=group_r2j_approved&ref=notif"
        )  # noqa: E502

    def save_recipe(id):
        """Saves recipe id to pickle file."""
        # TODO # get recipe id to save.
        s = logic.Sync()
        s.add_fav(id)

    def export(id):
        """Export recipe as pdf."""
        # TODO # get recipe info by id.

    def update_dropdown():
        Controller.update_dropdown_vis()
        Controller.update_dropdown_results()

    def update_dropdown_vis():
        if lpanel["search_bar"].text():
            lpanel["filter_dropdown"].setVisible(True)
        else:
            lpanel["filter_dropdown"].setVisible(False)

    def update_dropdown_results():
        lpanel["filter_dropdown"].clear()
        result_list = logic.Logic.get_matching_ingredients(
            lpanel["search_bar"].text()
        )
        if len(result_list) <= 8:
            lpanel["filter_dropdown"].setMaximumHeight(len(result_list) * 30)
        else:
            lpanel["filter_dropdown"].setMaximumHeight(200)

        lpanel["filter_dropdown"].addItems(result_list)

    def select_ingredient(ingr):
        logic.Logic.add_ingr_selected(ingr)
        Controller.update_dropdown()
        lpanel["search_bar"].clear()

    def update_results():
        lpanel["scroll_area"].removeWidget
        pass
