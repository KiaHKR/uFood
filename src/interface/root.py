"""Root file to carry root, Views and controller class."""
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from src.interface.panels.left_panel import Components as lcomp
from src.interface.panels.right_top_panel import Compontents as rtcomp
from src.interface.panels.right_bottom_panel import Components as rbcomp
import src.bin.logic as logic

# import bottom rpanel
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

    def __save_build(id):
        """Build save feature."""
        save = qtw.QPushButton()
        save.setLayout(qtw.QHBoxLayout())
        save.layout().addWidget(b_rpanel["save_btn"])
        save.setFixedSize(50, 50)
        save.clicked.connect(lambda: Controller.save(id))
        return save

    def __export_build(id):
        """Build export feature."""
        export = qtw.QPushButton()
        export.setLayout(qtw.QHBoxLayout())
        export.setFixedSize(50, 50)
        export.layout().addWidget(b_rpanel["export_btn"])
        export.clicked.connect(lambda: Controller.export(id))
        return export

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

        top_layout.addWidget(t_rpanel["back_btn"])
        top_layout.addWidget(t_rpanel["win_text"])
        top_layout.addWidget(t_rpanel["fav_btn"])
        top_layout.addWidget(t_rpanel["recipes_btn"])

        t_rpanel["recipes_btn"].clicked.connect(
            lambda: Controller.show_all_recipes()
        )

        widget = qtw.QWidget()
        widget.setLayout(top_layout)
        return widget

    # !-- Right bottom panel
    def __right_bottom_build(self):
        """Widget of right bottom panel."""
        Controller.build_trending()

    def __right_bottom_refresh(self):
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
        recipe_card = qtw.QWidget()
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

        recipe_card.layout().addWidget(rbcomp().thumbnail_img(thumbnail), 1)
        recipe_card.layout().addWidget(info, 9)
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

        recipe_card.layout().addWidget(buttons, 1)

        time.setLayout(qtw.QHBoxLayout())
        time.layout().addWidget(b_rpanel["total_time_icon"])
        time.layout().addWidget(rbcomp().total_time(total_time))
        time.layout().setContentsMargins(0, 0, 0, 0)
        time.layout().setSpacing(0)
        info.layout().addWidget(time)
        info.layout().addWidget(rbcomp().ingredients(ingr))
        info.layout().setContentsMargins(0, 0, 0, 0)
        info.layout().setSpacing(0)

        return recipe_card


class Controller:
    """Controller class."""

    pos = "Trending"

    def update_logo_size(left_panel_widget):
        """For changing size of logo pixmap, based on parent panel size."""
        lpanel["logo"].setPixmap(
            qtg.QPixmap(lcomp.path + "logo_placeholder.png").scaled(
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
        s = logic.Sync()
        s.add_fav(id)

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

        # Generate and delte recipe cards ---------

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

        no_recipes = qtw.QLabel("No recipes found!")
        no_recipes.setStyleSheet("color: white; font-size: 25px")
        no_recipes.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

        if len(widget_list) != 0:
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

    def delete_recipe_cards():
        """Clear scroll_area and remove it from the right_panel."""
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

    def show_all_recipes():
        """Show all recipes."""
        if Controller.pos != "All Recipes":
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
        if return_list is None:

            pass
        else:
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
        lpanel["time_label"].setText(str(lpanel["time_slider"].value()))
