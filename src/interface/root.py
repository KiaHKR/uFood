"""Root file to carry root, Views and controller class."""
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from src.interface.panels.left_panel import Components as lcomp
from src.interface.panels.right_top_panel import Compontents as rtcomp
from src.interface.panels.right_bottom_panel import Components as rbcomp
import src.bin.logic as logic
from src.interface.panels.right_bottom_panel import Components as comp
from src.bin import query


app = qtw.QApplication(os.sys.argv)
lpanel = lcomp().widgets
t_rpanel = rtcomp().widgets
b_rpanel = rbcomp().widgets


class Root(qtw.QWidget):
    """Parent class for containing ui."""

    def __init__(self, *args, **kwargs):
        """Is constructor of root class."""
        super().__init__(*args, **kwargs)
        # -- Build root panel
        layout = qtw.QHBoxLayout()
        self.screen = app.primaryScreen().size()
        self.resize(self.screen.width() // 2, self.screen.height() // 2)
        self.setStyleSheet("background-color: #1c1c1c;")
        self.setLayout(layout)
        self.setWindowTitle("uFood")
        self.setWindowIcon(
            qtg.QIcon(qtg.QPixmap(lcomp.path + "carrot_icon.png"))
        )


root_view = Root()


class View(qtw.QWidget):
    """Parent Layout for left and right widget."""

    def __init__(self, *args, **kwargs):
        """Contructor of view class."""
        super().__init__(*args, **kwargs)

        # left panel
        self.left_panel_widget = self.__left_panel_build()
        self.left_panel_widget.setMinimumWidth(300)
        root_view.layout().addWidget(self.left_panel_widget, 3)

        # right panel
        self.right_panel_widget = qtw.QWidget()
        self.right_panel_widget.setLayout(qtw.QVBoxLayout())

        # right top panel
        rtop_panel = self.__right_top_build()

        # right bottom panel
        self.__right_bottom_build()
        self.right_panel_widget.layout().addWidget(rtop_panel)

        self.right_panel_widget.layout().addWidget(b_rpanel["scroll_area"])
        self.right_panel_widget.setMinimumWidth(750)

        root_view.layout().addWidget(self.right_panel_widget, 7)

        self.qTimer = qtc.QTimer()
        self.qTimer.setInterval(1)
        self.qTimer.timeout.connect(
            lambda: Controller.update_logo_size(self.left_panel_widget)
        )
        self.qTimer.start()

        root_view.show()
        self.__right_bottom_refresh()

        os.sys.exit(app.exec_())

    # !-- Left Panel

    def __left_panel_build(self):
        """For building left panel."""
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

        # Logo goes to trending connection

        # filter_dropdown on select connection
        lpanel["filter_dropdown"].itemClicked.connect(
            lambda: Controller.select_ingredient(
                lpanel["filter_dropdown"].currentItem()
            )
        )

        # Construct search button
        search_icon_widget = qtw.QWidget()
        search_icon_widget.setLayout(qtw.QStackedLayout())

        # Connect filter btn to filter menu
        lpanel["search_filter_btn"].setMenu(lpanel["search_filter_menu"])

        # Search bar on change connection
        lpanel["search_bar"].textChanged.connect(
            lambda: Controller.update_dropdown()
        )

        # Search bar on return pressed connection
        lpanel["search_bar"].returnPressed.connect(
            lambda: Controller.update_name_search_results(
                lpanel["search_bar"].text()
            )
        )

        # Search button connection
        lpanel["search_btn"].pressed.connect(
            lambda: Controller.update_name_search_results(
                lpanel["search_bar"].text()
            )
        )

        # Selected ingredients on item clicked connection
        lpanel["selected_items"].itemClicked.connect(
            lambda: Controller.remove_ingredient(
                lpanel["selected_items"].currentItem()
            )
        )

        # Update slider time connector
        lpanel["time_slider"].valueChanged.connect(
            lambda: Controller.update_label()
        )

        # Update on slider released
        lpanel["time_slider"].sliderReleased.connect(
            lambda: Controller.update_slider()
        )

        # Update diet filter_dropdown menu on selection
        keto = lpanel["search_filter_menu"].findChild(qtw.QAction, "Keto")
        paleo = lpanel["search_filter_menu"].findChild(qtw.QAction, "Paleo")
        vegan = lpanel["search_filter_menu"].findChild(qtw.QAction, "Vegan")
        vegetarian = lpanel["search_filter_menu"].findChild(
            qtw.QAction, "Vegetarian"
        )
        keto.triggered.connect(
            lambda: Controller.update_diet_filter(
                [keto, paleo, vegan, vegetarian]
            )
        )
        paleo.triggered.connect(
            lambda: Controller.update_diet_filter(
                [keto, paleo, vegan, vegetarian]
            )
        )
        vegan.triggered.connect(
            lambda: Controller.update_diet_filter(
                [keto, paleo, vegan, vegetarian]
            )
        )
        vegetarian.triggered.connect(
            lambda: Controller.update_diet_filter(
                [keto, paleo, vegan, vegetarian]
            )
        )

        slider_hbox = qtw.QHBoxLayout()
        slider_hbox.addWidget(lpanel["time_slider"])
        slider_hbox.addSpacing(15)
        slider_hbox.addWidget(lpanel["time_label"])

        slider_widget = qtw.QWidget()
        slider_widget.setLayout(slider_hbox)
        slider_widget.setFixedHeight(30)
        slider_widget.setStyleSheet("background-color: transparent;")

        # Create stacked layout for selected ingr and drop down
        search_stack = qtw.QWidget()
        search_stack.setLayout(qtw.QStackedLayout())

        search_stack.layout().addWidget(lpanel["filter_dropdown"])
        search_stack.layout().addWidget(lpanel["selected_items"])
        # Add widgets to parent search layout
        search_widget.layout().addWidget(slider_widget, 0, 0)
        search_widget.layout().addWidget(lpanel["search_bar"], 1, 0)
        search_widget.layout().addWidget(search_stack, 2, 0)
        search_widget.layout().addWidget(lpanel["search_btn_bg"], 1, 2)
        search_widget.layout().addWidget(lpanel["search_btn"], 1, 2)
        search_widget.layout().addWidget(lpanel["search_filter_btn"], 1, 3)
        search_widget.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignTop)
        search_widget.layout().setSpacing(0)

        return search_widget

    def __export_build(id):
        """Build export feature."""
        export = qtw.QPushButton()
        export.setLayout(qtw.QHBoxLayout())
        export.setFixedSize(50, 50)
        export.layout().addWidget(b_rpanel["export_btn"])
        export.clicked.connect(lambda: Controller.export(id))
        return export

    def __save_build(id):
        """Build save feature."""
        save = qtw.QPushButton()
        save.setLayout(qtw.QHBoxLayout())
        save.layout().addWidget(comp().save_btn(id))
        save.setFixedSize(50, 50)
        save.clicked.connect(
            lambda: Controller.save(id),
            # lambda: Controller.update_favorites(),
        )
        # save.clicked.connect()
        return save

    def __donate_build(self):
        """Build donate feature."""
        donate = qtw.QPushButton()
        donate.setLayout(qtw.QHBoxLayout())
        donate.layout().addWidget(lpanel["donate_btn"], 0)
        donate.layout().addWidget(lpanel["donate_text"], 8)
        donate.setFixedSize(200, 50)
        donate.setStyleSheet("border: none;")
        donate.clicked.connect(lambda: Controller.donate_url())
        return donate

    # !-- Right Top Panel
    def __right_top_build(self):
        """For building right top panel."""
        top_layout = qtw.QHBoxLayout()

        top_layout.addWidget(t_rpanel["win_text"])
        top_layout.addWidget(t_rpanel["trending_btn"])
        top_layout.addWidget(t_rpanel["fav_btn"])
        top_layout.addWidget(t_rpanel["recipes_btn"])
        top_layout.addWidget(t_rpanel["settings_btn"])

        t_rpanel["recipes_btn"].clicked.connect(
            lambda: Controller.show_all_recipes()
        )

        t_rpanel["trending_btn"].clicked.connect(
            lambda: Controller.update_trending()
        )

        t_rpanel["settings_btn"].clicked.connect(
            lambda: Controller.build_settings(self)
        )

        widget = qtw.QWidget()
        widget.setLayout(top_layout)
        return widget

    # !-- Right bottom panel
    def __right_bottom_build(self):
        """Widget of right bottom panel."""
        Controller.build_trending()

    def __right_bottom_refresh(self):
        """Refresh the right bottom panel"""
        self.right_panel_widget.layout().addWidget(b_rpanel["scroll_area"])

    def recipe_card(
        name="[RECIPE NAME]",
        diet_type="[DIET TYPE]",
        total_time="[TOTAL TIME]",
        ingr="[INGREDIENT LIST]",
        pk_id="Error",
        thumbnail=None,
    ):
        """Widgets of recipe cards."""
        recipe_card = qtw.QPushButton()
        recipe_card.setLayout(qtw.QHBoxLayout())
        recipe_card.setStyleSheet(
            "QWidget::hover" "{background-color : #6c899d;}"
        )

        info = qtw.QWidget()
        info.setLayout(qtw.QVBoxLayout())
        info.setStyleSheet("background-color: transparent;")
        # info.setStyleSheet("border: none;")
        info.layout().addWidget(rbcomp().recipe_title(name))
        info.layout().addWidget(rbcomp().diet_type(diet_type))

        time = qtw.QWidget()

        recipe_card.setObjectName(pk_id)
        recipe_card.setFixedHeight(150)

        buttons = qtw.QWidget()
        buttons.setLayout(qtw.QVBoxLayout())
        buttons.setStyleSheet("background-color: transparent;")
        buttons.layout().addWidget(View.__save_build(recipe_card.objectName()))

        buttons.layout().addWidget(
            View.__export_build(recipe_card.objectName())
        )
        buttons.layout().setSpacing(0)

        recipe_card.layout().addWidget(rbcomp().thumbnail_img(thumbnail), 1)
        recipe_card.layout().addWidget(info, 20)
        recipe_card.layout().addWidget(buttons, 0)

        time.setLayout(qtw.QHBoxLayout())
        time.layout().addWidget(b_rpanel["total_time_icon"])
        time.layout().addWidget(rbcomp().total_time(total_time))
        time.layout().setContentsMargins(0, 0, 0, 0)
        time.layout().setSpacing(0)
        info.layout().addWidget(time)
        info.layout().addWidget(rbcomp().ingredients(ingr))
        info.layout().setContentsMargins(0, 0, 0, 0)
        info.layout().setSpacing(0)
        # recipe_card.setCursor(qtg.QCursor(qtc.Qt.OpenHandCursor))
        recipe_card.clicked.connect(
            lambda: Controller.export(recipe_card.objectName())
        )
        return recipe_card


class Controller:
    """Controller class."""

    pos = "Trending"
    recipes_cards_showing = []

    def update_logo_size(left_panel_widget):
        """For changing size of logo pixmap, based on parent panel size."""
        lpanel["logo"].setPixmap(
            qtg.QPixmap(lcomp.path + "ufood_logo.png").scaled(
                left_panel_widget.width() // 1.9,
                left_panel_widget.height() // 2.5,
                qtc.Qt.AspectRatioMode.KeepAspectRatio,
            )
        )
        lpanel["logo"].setFixedHeight(left_panel_widget.height() // 2.5)

    def donate_url():
        """Url link for Facebook group."""
        os.startfile(
            "https://www.facebook.com/groups/1454991488172182/?notif_id=1620038256343772&notif_t=group_r2j_approved&ref=notif"  # noqa: E501
        )

    def save(id):
        """For saving recipe id to pickle file."""
        s = logic.Logic()
        s.add_fav(id)
        win_text = t_rpanel["win_text"].text()
        if win_text == "Trending Recipes":
            Controller.update_trending()
        elif win_text == "Favorite Recipes":
            Controller.build_favorites()
        elif win_text == "All Recipes":
            Controller.show_all_recipes(force=True)
        elif "Search Results" in win_text:
            Controller.update_name_search_results(lpanel["search_bar"].text())

    def export(id):
        """Export recipe as pdf."""
        name, ingred, instructions, source = query.Search().get_export_info(id)
        logic.Pdf(name, ingred, instructions, source)

    # Dropdown from search bar update -----

    def update_dropdown():
        """Update results of dropdown."""
        if lpanel["search_bar"].text():
            lpanel["filter_dropdown"].setVisible(True)
        else:
            lpanel["filter_dropdown"].setVisible(False)
            if len(logic.selected_ingredients) > 0:
                Controller.update_ingredient_search_results()
            elif t_rpanel["win_text"].text() != "Trending Recipes":
                Controller.update_trending()

        lpanel["filter_dropdown"].clear()
        result_list = logic.Logic.get_matching_ingredients(
            lpanel["search_bar"].text()
        )
        if len(result_list) <= 8:
            lpanel["filter_dropdown"].setMaximumHeight(len(result_list) * 30)
        else:
            lpanel["filter_dropdown"].setMaximumHeight(200)

        lpanel["filter_dropdown"].addItems(result_list)

    # Select and remove selected ingredients -----

    def select_ingredient(ingr):
        """For selecting ingredients."""
        logic.Logic.add_ingr_selected(ingr)
        Controller.update_dropdown()
        Controller.update_selected()
        lpanel["search_bar"].clear()
        Controller.update_ingredient_search_results()

    def remove_ingredient(ingr):
        """For removing ingredients."""
        logic.Logic.remove_ingr_selected(ingr)
        Controller.update_dropdown()
        Controller.update_selected()
        if len(logic.selected_ingredients) > 0:
            Controller.update_ingredient_search_results()
        else:
            Controller.update_trending()

    # Update the list of selected ingredients ------

    def update_selected():
        """Update visibility of selected ingr."""
        if len(logic.selected_ingredients) != 0:
            lpanel["selected_items"].setVisible(True)
        else:
            lpanel["selected_items"].setVisible(False)
        lpanel["selected_items"].clear()
        lpanel["selected_items"].addItems(logic.selected_ingredients)

    # Trending build and update --------

    def build_trending():
        """Update_trending(), but only used on initial build."""
        trending_list = logic.Logic.get_trending()
        Controller.generate_recipe_cards(trending_list, build=True)
        Controller.update_section_header("Trending Recipes")

    def update_trending():
        """Generate the VBox widget with the list of trending recipes."""
        Controller.delete_recipe_cards()
        trending_list = logic.Logic.get_trending()
        Controller.generate_recipe_cards(trending_list)
        Controller.update_section_header("Trending Recipes")
        Controller.clear_tags()

    def build_favorites():
        """Build favorite recipe cards."""
        Controller.delete_recipe_cards()
        Controller.update_section_header("Favorite Recipes")
        favorite_list = logic.Logic.get_favorites()
        Controller.generate_recipe_cards(favorite_list)

    def update_favorites():
        """Update title to favorites."""
        win_text = t_rpanel["win_text"]
        if win_text == "Favorite Recipes":
            Controller.build_favorites()

    def build_settings(self):
        """Build the settings feature."""

        settings = Controller.settings_panel()
        for i in reversed(
            range(b_rpanel["scroll_area"].widget().layout().count())
        ):
            remove_widget = (
                b_rpanel["scroll_area"].widget().layout().takeAt(i).widget()
            )
            b_rpanel["scroll_area"].widget().layout().removeWidget(
                remove_widget
            )
            remove_widget.deleteLater()
        Controller.update_section_header("Settings")
        settings.setObjectName("settings")
        settings.setFixedHeight(root_view.children()[2].height() * 0.8)
        panel_box = root_view.children()[2].children()[0].layout()
        panel_box.addWidget(settings, 10000)  # some ridiculous stretch margin

    def settings_panel():
        """Build the widgets associated with the settings feature."""
        settings = qtw.QWidget()
        settings.setLayout(qtw.QVBoxLayout())
        import_export = qtw.QWidget()
        import_export.setLayout(qtw.QHBoxLayout())
        import_btn = qtw.QPushButton("Import Favorites")
        export_btn = qtw.QPushButton("Export Favorites")
        import_export.layout().addWidget(import_btn)
        import_export.layout().addWidget(export_btn)
        install_location = qtw.QLineEdit()
        install_location.setPlaceholderText(
            logic.Sync.pickle_getDownloadPath()
        )
        install_location.setFixedHeight(30)
        options = qtw.QWidget()
        options.setLayout(qtw.QHBoxLayout())
        submit_btn = qtw.QPushButton("Submit")
        clear_btn = qtw.QPushButton("Clear")

        # styling buttons
        background = "white"
        install_location.setStyleSheet(f"background: {background}")
        import_btn.setStyleSheet(
            f"background: {background}; font-size: 14px; font-weight: bold;"
        )
        export_btn.setStyleSheet(
            f"background: {background}; font-size: 14px; font-weight: bold;"
        )
        clear_btn.setStyleSheet(f"background: {background};")
        submit_btn.setStyleSheet(f"background: {background};")

        options.layout().addWidget(clear_btn)
        options.layout().addWidget(submit_btn)
        empty_space = qtw.QWidget()

        # add widgets to settings

        settings.layout().addWidget(import_export, 1)
        settings.layout().addWidget(empty_space, 1)
        settings.layout().addWidget(install_location, 1)
        settings.layout().addWidget(options, 1)
        settings.show()
        return settings

    def generate_recipe_cards(recipe_list, build=False):
        """Generate a VBox with a list of recipe cards in it."""
        widget_list = []
        for i in recipe_list:
            recipe_card = View.recipe_card(
                i[0].title(),  # NAME
                i[2].replace(",", ", "),
                str(i[1])[:-3],  # COOKTIME
                i[3].replace(",", ", "),
                str(i[4]),  # ID
                i[5],  # URL
            )
            widget_list.append(recipe_card)
        Controller.build_recipe_cards(widget_list, build)

    def build_recipe_cards(widget_list, build=False):
        """Add recipe cards from widget_list to scroll_area."""
        no_recipes = qtw.QLabel("No recipes found!")
        no_recipes.setStyleSheet("color: white; font-size: 25px")
        no_recipes.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

        if len(widget_list) > 0:
            for i in range(len(widget_list)):
                b_rpanel["scroll_area"].widget().layout().addWidget(
                    widget_list[i]
                )
        else:
            b_rpanel["scroll_area"].widget().layout().addWidget(no_recipes)

        if not build:
            root_view.children()[2].children()[0].layout().addWidget(
                b_rpanel["scroll_area"]
            )
        Controller.recipes_cards_showing = widget_list

    def delete_recipe_cards():
        """Clear scroll_area and remove it from the right_panel."""
        if Controller.pos == "Settings":
            rmwidget = root_view.children()[2].findChild(
                qtw.QWidget, "settings"
            )
            root_view.children()[2].children()[0].layout().removeWidget(
                rmwidget
            )

        for i in reversed(
            range(b_rpanel["scroll_area"].widget().layout().count())
        ):
            remove_widget = (
                b_rpanel["scroll_area"].widget().layout().takeAt(i).widget()
            )
            b_rpanel["scroll_area"].widget().layout().removeWidget(
                remove_widget
            )
            remove_widget.deleteLater()

        root_view.children()[2].children()[0].removeWidget(
            b_rpanel["scroll_area"]
        )

    # Section management ---------

    def update_section_header(text):
        """Update section title."""
        Controller.pos = text
        t_rpanel["win_text"].setText(text)

    def show_all_recipes(force=False):
        """Show all recipes."""
        if Controller.pos != "All Recipes" or force:
            Controller.clear_tags()
            Controller.delete_recipe_cards()
            recipes = logic.Logic.name_search(
                None, lpanel["time_slider"].value()
            )
            Controller.generate_recipe_cards(recipes)
            Controller.update_section_header("All Recipes")

    def clear_tags():
        """Clear selected ingredient."""
        logic.selected_ingredients = []
        Controller.update_selected()

    # Different search methods -------

    def update_ingredient_search_results():
        """Update ingredient_search results."""
        Controller.delete_recipe_cards()
        result_list = logic.Logic.get_ingredient_search(
            lpanel["time_slider"].value()
        )
        Controller.generate_recipe_cards(result_list)
        Controller.update_section_header(
            str(len(result_list)) + " Search Results"
        )

    def update_name_search_results(search):
        """Search recipes by name and selected ingr."""
        return_list = logic.Logic.name_search(
            search, lpanel["time_slider"].value()
        )
        if return_list is not None:
            Controller.generate_recipe_cards(return_list)
            Controller.update_section_header(
                str(len(return_list)) + " Search Results"
            )

    def update_slider():
        """Update search results when slider released."""
        if t_rpanel["win_text"].text() == "Trending Recipes":
            pass
        elif t_rpanel["win_text"].text() == "All Recipes":
            Controller.update_name_search_results(None)
        else:
            Controller.update_name_search_results(lpanel["search_bar"].text())

    def update_label():
        """Update slider label."""
        lpanel["time_label"].setText(
            "Cook time: " + str(lpanel["time_slider"].value()) + "min"
        )

    def update_diet_filter(diet_type_list):
        """Update the search result by dietary filter."""
        final_list = Controller.recipes_cards_showing
        Controller.hide_remaining_cards(Controller.recipes_cards_showing)
        Not_selected = 0
        for diet_type in diet_type_list:
            if diet_type is not None and diet_type.isChecked():
                diet_type = diet_type.text()
                recipes_to_filter = final_list
                filtered = list(
                    filter(
                        lambda x: diet_type
                        in str(x.findChild(qtw.QLabel, "diet_type").text()),
                        recipes_to_filter,
                    )
                )
                final_list = filtered
            elif diet_type is not None and not diet_type.isChecked():
                Not_selected += 1

        if Not_selected == 4:
            final_list = Controller.recipes_cards_showing

        Controller.restore_cards(final_list)

    def hide_remaining_cards(list_to_hide):
        """Hide all recipes from the filtered list."""
        for recipe in list_to_hide:
            recipe.hide()

    def restore_cards(restore_list):
        """Restore all the cards per the class variable."""
        for recipe in restore_list:
            recipe.show()
