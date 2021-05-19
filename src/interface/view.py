import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

import src.interface.controller as controller
import src.interface.view_builder as view_builder
import src.interface.globals as globals
import src.interface.panels.right_bottom_panel as rbcomp


class View(qtw.QWidget):
    """Parent Layout for left and right widget."""

    def __init__(self, *args, **kwargs):
        """Contructor of view class."""
        super().__init__(*args, **kwargs)

        # left panel
        self.left_panel_widget = self.__left_panel_build()
        self.left_panel_widget.setMinimumWidth(300)
        globals.Globals.root_view.layout().addWidget(self.left_panel_widget, 3)

        # right panel
        self.right_panel_widget = qtw.QWidget()
        self.right_panel_widget.setLayout(qtw.QVBoxLayout())

        # right top panel
        rtop_panel = self.__right_top_build()

        # right bottom panel
        self.__right_bottom_build()
        self.right_panel_widget.layout().addWidget(rtop_panel)

        globals.Globals.stacked_widget = View.stacked_layout_build()

        self.right_panel_widget.layout().addWidget(
            globals.Globals.stacked_widget
        )
        self.right_panel_widget.setMinimumWidth(750)

        globals.Globals.root_view.layout().addWidget(
            self.right_panel_widget, 7
        )

        self.qTimer = qtc.QTimer()
        self.qTimer.setInterval(1)
        self.qTimer.timeout.connect(
            lambda: controller.Controller.update_logo_size(
                self.left_panel_widget
            )
        )
        self.qTimer.start()

        globals.Globals.root_view.show()

        os.sys.exit(globals.Globals.app.exec_())

    # !-- Left Panel

    def __left_panel_build(self):
        """For building left panel."""
        left_panel_widget = qtw.QWidget()
        left_panel_widget.setLayout(qtw.QVBoxLayout())
        controller.Controller.update_logo_size(
            left_panel_widget
        )  # Grabbing logo size from window size
        left_panel_widget.layout().addWidget(globals.Globals.lpanel["logo"])
        left_panel_widget.layout().addWidget(self.__search_widget_build())
        left_panel_widget.layout().addWidget(self.__donate_build())
        return left_panel_widget

    def __search_widget_build(self):
        """Build parent search widget."""
        search_widget = qtw.QWidget()
        search_widget.setLayout(qtw.QGridLayout())

        # filter_dropdown on select connection
        globals.Globals.lpanel["filter_dropdown"].itemClicked.connect(
            lambda: controller.Controller.select_ingredient(
                globals.Globals.lpanel["filter_dropdown"].currentItem()
            )
        )

        # Construct search button
        search_icon_widget = qtw.QWidget()
        search_icon_widget.setLayout(qtw.QStackedLayout())

        # Connect filter btn to filter menu
        globals.Globals.lpanel["search_filter_btn"].setMenu(
            globals.Globals.lpanel["search_filter_menu"]
        )

        # Search bar on change connection
        globals.Globals.lpanel["search_bar"].textEdited.connect(
            lambda: controller.Controller.update_dropdown()
        )

        # Search bar on return pressed connection
        globals.Globals.lpanel["search_bar"].returnPressed.connect(
            lambda: controller.Controller.update_name_search_results(
                globals.Globals.lpanel["search_bar"].text()
            )
        )

        # Search button connection
        globals.Globals.lpanel["search_btn"].pressed.connect(
            lambda: controller.Controller.update_name_search_results(
                globals.Globals.lpanel["search_bar"].text()
            )
        )

        # Selected ingredients on item clicked connection
        globals.Globals.lpanel["selected_items"].itemClicked.connect(
            lambda: controller.Controller.remove_ingredient(
                globals.Globals.lpanel["selected_items"].currentItem()
            )
        )

        # Update slider time connector
        globals.Globals.lpanel["time_slider"].valueChanged.connect(
            lambda: controller.Controller.update_label()
        )

        # Update on slider released
        globals.Globals.lpanel["time_slider"].sliderReleased.connect(
            lambda: controller.Controller.update_slider()
        )

        # Update diet filter_dropdown menu on selection
        keto = globals.Globals.lpanel["search_filter_menu"].findChild(
            qtw.QAction, "Keto"
        )
        paleo = globals.Globals.lpanel["search_filter_menu"].findChild(
            qtw.QAction, "Paleo"
        )
        vegan = globals.Globals.lpanel["search_filter_menu"].findChild(
            qtw.QAction, "Vegan"
        )
        vegetarian = globals.Globals.lpanel["search_filter_menu"].findChild(
            qtw.QAction, "Vegetarian"
        )
        keto.triggered.connect(
            lambda: controller.Controller.update_diet_filter(
                [keto, paleo, vegan, vegetarian]
            )
        )
        paleo.triggered.connect(
            lambda: controller.Controller.update_diet_filter(
                [keto, paleo, vegan, vegetarian]
            )
        )
        vegan.triggered.connect(
            lambda: controller.Controller.update_diet_filter(
                [keto, paleo, vegan, vegetarian]
            )
        )
        vegetarian.triggered.connect(
            lambda: controller.Controller.update_diet_filter(
                [keto, paleo, vegan, vegetarian]
            )
        )

        slider_hbox = qtw.QHBoxLayout()
        slider_hbox.addWidget(globals.Globals.lpanel["time_slider"])
        slider_hbox.addSpacing(15)
        slider_hbox.addWidget(globals.Globals.lpanel["time_label"])

        slider_widget = qtw.QWidget()
        slider_widget.setLayout(slider_hbox)
        slider_widget.setFixedHeight(30)
        slider_widget.setStyleSheet("background-color: transparent;")

        # Create stacked layout for selected ingr and drop down
        search_stack = qtw.QWidget()
        search_stack.setLayout(qtw.QStackedLayout())

        search_stack.layout().addWidget(
            globals.Globals.lpanel["filter_dropdown"]
        )
        search_stack.layout().addWidget(
            globals.Globals.lpanel["selected_items"]
        )
        # Add widgets to parent search layout
        search_widget.layout().addWidget(slider_widget, 0, 0)
        search_widget.layout().addWidget(
            globals.Globals.lpanel["search_bar"], 1, 0
        )
        search_widget.layout().addWidget(search_stack, 2, 0)
        search_widget.layout().addWidget(
            globals.Globals.lpanel["search_btn_bg"], 1, 2
        )
        search_widget.layout().addWidget(
            globals.Globals.lpanel["search_btn"], 1, 2
        )
        search_widget.layout().addWidget(
            globals.Globals.lpanel["search_filter_btn"], 1, 3
        )
        search_widget.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignTop)
        search_widget.layout().setSpacing(0)

        return search_widget

    def export_build(id):
        """Build export feature."""
        export = qtw.QPushButton()
        export.setLayout(qtw.QHBoxLayout())
        export.setFixedSize(50, 50)
        export.layout().addWidget(globals.Globals.b_rpanel["export_btn"])
        export.clicked.connect(lambda: controller.Controller.export(id))
        return export

    

    def __donate_build(self):
        """Build donate feature."""
        donate = qtw.QPushButton()
        donate.setLayout(qtw.QHBoxLayout())
        donate.layout().addWidget(globals.Globals.lpanel["donate_btn"], 0)
        donate.layout().addWidget(globals.Globals.lpanel["donate_text"], 8)
        donate.setFixedSize(200, 50)
        donate.setStyleSheet("border: none;")
        donate.clicked.connect(lambda: controller.Controller.donate_url())
        return donate

    # !-- Right Top Panel
    def __right_top_build(self):
        """For building right top panel."""
        top_layout = qtw.QHBoxLayout()

        top_layout.addWidget(globals.Globals.t_rpanel["win_text"])
        top_layout.addWidget(globals.Globals.t_rpanel["trending_btn"])
        top_layout.addWidget(globals.Globals.t_rpanel["fav_btn"])
        top_layout.addWidget(globals.Globals.t_rpanel["recipes_btn"])
        top_layout.addWidget(globals.Globals.t_rpanel["settings_btn"])

        globals.Globals.t_rpanel["recipes_btn"].clicked.connect(
            lambda: controller.Controller.show_all_recipes()
        )

        globals.Globals.t_rpanel["trending_btn"].clicked.connect(
            lambda: controller.Controller.update_trending()
        )

        globals.Globals.t_rpanel["settings_btn"].clicked.connect(
            lambda: controller.Controller.build_settings(self)
        )

        widget = qtw.QWidget()
        widget.setLayout(top_layout)
        return widget

    # !-- Right bottom panel
    def __right_bottom_build(self):
        """Widget of right bottom panel."""
        controller.Controller.build_trending()

    def stacked_layout_build():
        """Refresh of right_bottom."""
        globals.Globals.stacked_widget = qtw.QWidget()
        globals.Globals.stacked_widget.setLayout(qtw.QStackedLayout())

        globals.Globals.recipe_view = (
            view_builder.ViewBuilder.build_recipe_view()
        )

        globals.Globals.stacked_widget.layout().addWidget(
            globals.Globals.b_rpanel["scroll_area"]
        )
        globals.Globals.stacked_widget.layout().addWidget(
            globals.Globals.recipe_view
        )
        return globals.Globals.stacked_widget