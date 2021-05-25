import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

import src.interface.globals as globals
import src.bin.logic as logic
import src.bin.query as query
import src.interface.panels.left_panel as lcomp
import src.interface.panels.right_bottom_panel as rbcomp
import src.interface.view_builder as view_builder

import src.bin.timeit as timeit


class Controller:
    """Controller class."""

    pos = "Trending"
    recipes_cards_showing = []
    saved_scroll_area = globals.Globals.b_rpanel["scroll_area"]
    widget_list = []
    delete_list = []
    raw_list = []

    def update_logo_size(left_panel_widget):
        """For changing size of logo pixmap, based on parent panel size."""
        globals.Globals.lpanel["logo"].setPixmap(
            qtg.QPixmap(lcomp.Components.path + "ufood_logo.png").scaled(
                left_panel_widget.width() // 1.9,
                left_panel_widget.height() // 2.5,
                qtc.Qt.AspectRatioMode.KeepAspectRatio,
            )
        )
        globals.Globals.lpanel["logo"].setFixedHeight(
            left_panel_widget.height() // 2.5
        )

    def donate_url():
        """Url link for Facebook group."""
        os.startfile(
            "https://www.facebook.com/groups/1454991488172182/?notif_id=1620038256343772&notif_t=group_r2j_approved&ref=notif"  # noqa: E501
        )

    def save(id):
        """For saving recipe id to pickle file."""
        s = logic.Logic()
        s.add_fav(id)
        Controller.update_fav(id)
        win_text = globals.Globals.t_rpanel["win_text"].text()
        if win_text == "Trending Recipes":
            Controller.update_trending()
        elif win_text == "Favorite Recipes":
            Controller.build_favorites()
        elif win_text == "All Recipes":
            Controller.show_all_recipes(force=True)
        elif "Search Results" in win_text:
            Controller.update_name_search_results(
                globals.Globals.lpanel["search_bar"].text()
            )

    def update_fav(id):
        scroll_pos = (
            globals.Globals.stacked_widget.findChild(
                qtw.QScrollArea, "scroll_area"
            )
            .verticalScrollBar()
            .value()
        )
        Controller.generate_recipe_cards(Controller.raw_list, force_update=id)

        globals.Globals.b_rpanel["scroll_area"].verticalScrollBar().setValue(
            scroll_pos
        )

    def export(id):
        """Export recipe as pdf."""
        name, ingred, instructions, source = query.Search().get_export_info(id)
        logic.Pdf(name, ingred, instructions, source)

    # ------------------- Dropdown from search bar update ------------------- #

    def update_dropdown():
        """Update results of dropdown."""
        if globals.Globals.lpanel["search_bar"].text():
            globals.Globals.lpanel["filter_dropdown"].setVisible(True)

            globals.Globals.lpanel["filter_dropdown"].clear()
            result_list = logic.Logic.get_matching_ingredients(
                globals.Globals.lpanel["search_bar"].text()
            )
            if len(result_list) <= 8:
                globals.Globals.lpanel["filter_dropdown"].setMaximumHeight(
                    len(result_list) * 30
                )
            else:
                globals.Globals.lpanel["filter_dropdown"].setMaximumHeight(200)

            globals.Globals.lpanel["filter_dropdown"].addItems(result_list)
        else:
            globals.Globals.lpanel["filter_dropdown"].setVisible(False)
            if len(logic.selected_ingredients) > 0:
                Controller.update_name_search_results("")
            else:
                Controller.update_trending()

    # ---------------- Select and remove selected ingredients --------------- #

    def select_ingredient(ingr):
        """For selecting ingredients."""
        logic.Logic.add_ingr_selected(ingr)
        Controller.update_dropdown()
        Controller.update_selected()
        Controller.update_ingredient_search_results()
        globals.Globals.lpanel["search_bar"].clear()
        globals.Globals.lpanel["filter_dropdown"].setVisible(False)

    def remove_ingredient(ingr):
        """For removing ingredients."""
        logic.Logic.remove_ingr_selected(ingr)
        Controller.update_selected()
        if len(logic.selected_ingredients) > 0:
            Controller.update_ingredient_search_results()
        else:
            Controller.update_trending()

    # --------------- Update the list of selected ingredients --------------- #

    def update_selected():
        """Update visibility of selected ingr."""
        if len(logic.selected_ingredients) != 0:
            globals.Globals.lpanel["selected_items"].setVisible(True)
        else:
            globals.Globals.lpanel["selected_items"].setVisible(False)
        globals.Globals.lpanel["selected_items"].clear()
        globals.Globals.lpanel["selected_items"].addItems(
            logic.selected_ingredients
        )

    # ---------------------- Trending build and update ---------------------- #

    def build_trending():
        """Update_trending(), but only used on initial build."""
        trending_list = logic.Logic.get_trending()
        Controller.generate_recipe_cards(trending_list, build=True)
        Controller.update_section_header("Trending Recipes")

    def update_trending():
        """Generate the VBox widget with the list of trending recipes."""
        trending_list = logic.Logic.get_trending()
        Controller.generate_recipe_cards(trending_list)
        # Controller.delete_recipe_cards()
        Controller.update_section_header("Trending Recipes")
        Controller.clear_tags()

    # ---------------------- Favorites build and update --------------------- #

    def build_favorites():
        """Build favorite recipe cards."""
        # Controller.update_section_header("Favorite Recipes")
        favorite_list = logic.Logic.get_favorites()
        Controller.generate_recipe_cards(favorite_list)
        # Controller.delete_recipe_cards()

    def update_favorites():
        """Update title to favorites."""
        win_text = globals.Globals.t_rpanel["win_text"]
        if win_text == "Favorite Recipes":
            Controller.build_favorites()

    def build_settings(self):
        """Build the settings feature."""
        if Controller.pos == "Settings":
            rmwidget = globals.Globals.root_view.children()[2].findChild(
                qtw.QWidget, "settings"
            )
            globals.Globals.root_view.children()[2].children()[
                0
            ].layout().removeWidget(rmwidget)
        settings = Controller.settings_panel()
        for i in reversed(
            range(
                globals.Globals.b_rpanel["scroll_area"]
                .widget()
                .layout()
                .count()
            )
        ):
            remove_widget = (
                globals.Globals.b_rpanel["scroll_area"]
                .widget()
                .layout()
                .takeAt(i)
                .widget()
            )
            globals.Globals.b_rpanel[
                "scroll_area"
            ].widget().layout().removeWidget(remove_widget)
            remove_widget.deleteLater()
        Controller.update_section_header("Settings")
        settings.setObjectName("settings")
        settings.setFixedHeight(
            globals.Globals.root_view.children()[2].height() * 0.8
        )
        panel_box = (
            globals.Globals.root_view.children()[2].children()[0].layout()
        )
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
        import_export.layout().setSpacing(150)

        options = qtw.QWidget()
        options.setLayout(qtw.QHBoxLayout())
        submit_btn = qtw.QPushButton("Submit")
        clear_btn = qtw.QPushButton("Clear")
        empty_space = qtw.QWidget()
        # styling buttons
        background = "white"
        styling = (
            f"background: {background}; font-size: 14px; font-weight: bold;"
        )

        import_btn.setFixedWidth(
            globals.Globals.root_view.children()[2].width() // 3
        )
        export_btn.setFixedWidth(
            globals.Globals.root_view.children()[2].width() // 3
        )
        import_btn.setStyleSheet(styling)

        export_btn.setStyleSheet(styling)
        clear_btn.setStyleSheet(styling)
        submit_btn.setStyleSheet(styling)

        options.layout().addWidget(clear_btn)
        options.layout().addWidget(submit_btn)

        # add widgets to settings
        settings.layout().setSpacing(20)
        settings.layout().addWidget(import_export, 1)
        settings.layout().addWidget(empty_space, 8)
        settings.show()

        # --- [SIGNALS]
        export_btn.clicked.connect(lambda: logic.Sync.export_favorites())
        import_btn.clicked.connect(
            lambda: Controller.import_btn_slot(import_btn)
        )

        return settings

    def import_btn_slot(parent_widget_object):
        """Import button slot."""
        filename = qtw.QFileDialog.getOpenFileName(
            parent_widget_object,
            "Open File",
            "uFridge",
            "Text Document (*.txt)",
        )
        if os.path.exists(filename[0]):
            logic.Sync.sync_to_fav(filename[0])

    # ------------------- Generate and delte recipe cards ------------------- #

    def generate_recipe_cards(recipe_list, build=False, force_update=None):
        """Generate a VBox with a list of recipe cards in it."""
        Controller.raw_list = recipe_list
        temp_widget_list = []
        for i in recipe_list:
            found_card = False
            for card in Controller.widget_list:
                try:
                    if (
                        str(i[4]) == card.objectName()
                        and str(i[4]) != force_update
                    ):
                        recipe_card = card
                        found_card = True
                        break
                except RuntimeError:
                    found_card = False
                    break

            if not found_card:
                recipe_card = view_builder.ViewBuilder.recipe_card(
                    i[0].title(),  # NAME
                    i[2].replace(",", ", "),
                    str(i[1])[:-3],  # COOKTIME
                    i[3].replace(",", ", "),
                    str(i[4]),  # ID
                    None,  # URL
                )

            temp_widget_list.append(recipe_card)

        Controller.delete_list = list(
            set(Controller.widget_list) - set(temp_widget_list)
        )
        Controller.widget_list = temp_widget_list

        Controller.build_recipe_cards(build)

    def build_recipe_cards(build=False):
        """Add recipe cards from widget_list to scroll_area."""
        no_recipes = qtw.QLabel("No recipes found!")
        no_recipes.setStyleSheet("color: white; font-size: 25px")
        no_recipes.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

        Controller.delete_recipe_cards()

        if len(Controller.widget_list) > 0:
            for i in range(len(Controller.widget_list)):
                globals.Globals.b_rpanel[
                    "scroll_area"
                ].widget().layout().addWidget(Controller.widget_list[i])
        else:
            globals.Globals.b_rpanel[
                "scroll_area"
            ].widget().layout().addWidget(no_recipes)

        if not build:

            globals.Globals.stacked_widget.layout().removeWidget(
                globals.Globals.stacked_widget.findChild(
                    qtw.QScrollArea, "scroll_area"
                )
            )
            globals.Globals.stacked_widget.layout().addWidget(
                globals.Globals.b_rpanel["scroll_area"]
            )
            globals.Globals.stacked_widget.layout().setCurrentWidget(
                globals.Globals.b_rpanel["scroll_area"]
            )

    def delete_recipe_cards():
        """Clear scroll_area and remove it from the right_panel."""
        if Controller.pos == "Settings":
            rmwidget = globals.Globals.root_view.children()[2].findChild(
                qtw.QWidget, "settings"
            )
            globals.Globals.root_view.children()[2].children()[
                0
            ].layout().removeWidget(rmwidget)

        for i in reversed(
            range(
                globals.Globals.b_rpanel["scroll_area"]
                .widget()
                .layout()
                .count()
            )
        ):
            remove_widget = (
                globals.Globals.b_rpanel["scroll_area"]
                .widget()
                .layout()
                .takeAt(i)
                .widget()
            )
            if remove_widget in Controller.delete_list:
                globals.Globals.b_rpanel[
                    "scroll_area"
                ].widget().layout().removeWidget(remove_widget)
                remove_widget.deleteLater()

    # -------------------------- Section management ------------------------- #

    def update_section_header(text):
        """Update section title."""
        if Controller.pos != text:
            globals.Globals.b_rpanel[
                "scroll_area"
            ].verticalScrollBar().setValue(0)

        if text == "40 Search Results":
            text = "All Recipes"

        Controller.pos = text
        globals.Globals.t_rpanel["win_text"].setText(text)

    def show_all_recipes(force=False):
        """Show all recipes."""
        if Controller.pos != "All Recipes" or force:
            Controller.clear_tags()
            # Controller.delete_recipe_cards()
            recipes = logic.Logic.name_search(
                None, globals.Globals.lpanel["time_slider"].value()
            )
            Controller.generate_recipe_cards(recipes)
            Controller.update_section_header("All Recipes")

    def clear_tags():
        """Clear selected ingredient."""
        logic.selected_ingredients = []
        Controller.update_selected()

    # ----------------------- Different search methods ---------------------- #

    # Search by ingredients
    def update_ingredient_search_results():
        """Update ingredient_search results."""
        result_list = logic.Logic.get_ingredient_search(
            globals.Globals.lpanel["time_slider"].value()
        )
        Controller.generate_recipe_cards(result_list)
        # Controller.delete_recipe_cards()
        Controller.update_section_header(
            str(len(result_list)) + " Search Results"
        )

    # Search by name
    def update_name_search_results(search):
        """Search recipes by name and selected ingr."""
        return_list = logic.Logic.name_search(
            search, globals.Globals.lpanel["time_slider"].value()
        )
        print(return_list)
        if return_list is not None:
            Controller.generate_recipe_cards(return_list)
            # Controller.delete_recipe_cards()
            Controller.update_section_header(
                str(len(return_list)) + " Search Results"
            )

    # Search by time
    def update_slider():
        """Update search results when slider released."""
        if globals.Globals.t_rpanel["win_text"].text() == "Trending Recipes":
            Controller.update_name_search_results(None)
        elif globals.Globals.t_rpanel["win_text"].text() == "All Recipes":
            Controller.update_name_search_results(None)
        else:
            Controller.update_name_search_results(None)

    # Update time label
    def update_label():
        """Update slider label."""
        globals.Globals.lpanel["time_label"].setText(
            "Cook time: "
            + str(globals.Globals.lpanel["time_slider"].value())
            + "min"
        )

    # Search by diets
    def update_diet_filter(diet_type_list):
        """Update the search result by dietary filter."""
        final_list = Controller.widget_list
        Controller.hide_remaining_cards(Controller.widget_list)
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
            final_list = Controller.widget_list

        Controller.restore_cards(final_list)

    # Hide cards passed in list
    def hide_remaining_cards(list_to_hide):
        """Hide all recipes from the filtered list."""
        for recipe in list_to_hide:
            recipe.hide()

    # Show cards passed in list
    def restore_cards(restore_list):
        """Restore all the cards per the class variable."""
        for recipe in restore_list:
            recipe.show()

    # ----------------------------- Recipe view ----------------------------- #

    # Run when recipe clicked
    def recipe_clicked(id):
        """Run when recipe card has been clicked."""
        Controller.update_recipe_view(id)
        Controller.set_recipe_view_vis(True)
        logic.Logic.add_view(id)

    def set_recipe_view_vis(view: bool):
        """Set recipe view visibility."""
        if not view:
            globals.Globals.b_rpanel[
                "scroll_area"
            ] = Controller.saved_scroll_area
            globals.Globals.stacked_widget.layout().setCurrentWidget(
                globals.Globals.b_rpanel["scroll_area"]
            )
        elif view:
            Controller.saved_scroll_area = (
                globals.Globals.stacked_widget.layout().currentWidget()
            )
            globals.Globals.stacked_widget.layout().setCurrentWidget(
                globals.Globals.recipe_view
            )

    # Update data in recipe view
    def update_recipe_view(id):
        """Update data in recipe view."""
        globals.Globals.stacked_widget.layout().removeWidget(
            globals.Globals.recipe_view
        )

        result = logic.Logic.get_recipe_info(id)

        globals.Globals.b_rpanel[
            "recipe_view_img"
        ] = rbcomp.Components().thumbnail_img(result[1])
        globals.Globals.b_rpanel["recipe_view_title"].setText(result[0])
        globals.Globals.b_rpanel["recipe_view_ingredients"].setText(result[2])
        globals.Globals.b_rpanel["recipe_view_steps"].setText(result[3])
        globals.Globals.b_rpanel["recipe_view_cook_diet_label"].setText(
            result[4]
        )

        globals.Globals.recipe_view = (
            view_builder.ViewBuilder.build_recipe_view()
        )

        globals.Globals.stacked_widget.layout().addWidget(
            globals.Globals.recipe_view
        )
