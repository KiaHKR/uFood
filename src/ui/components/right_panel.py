"""A class covering builds for the right top panel and right bottom panel"""

from ui.components.templates.media_widgets import MediaWidgets
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class RightTopPanel:
    """Contains all functionality for building the right top-most panel."""

    def __init__(self):
        """Build constructor."""
        self.r_top = qtw.QWidget()
        self.r_top.setLayout(qtw.QHBoxLayout())
        self.r_top.setFixedHeight(40)

    def build_panel(self, input_text=None):
        """Build top panel."""
        if input_text is not None:
            input_text = self.__set_text(input_text)

        favorites_icon = self.__set_toolbar_icon('fav_icon.png')
        recipes_icon = self.__set_toolbar_icon('recipes_icon.png')
        back_icon = self.__set_toolbar_icon('back_icon.png')
        self.r_top.layout().addWidget(back_icon, 1)
        self.r_top.layout().addWidget(input_text, 9)
        self.r_top.layout().addWidget(favorites_icon, 1)
        self.r_top.layout().addWidget(recipes_icon, 1)
        return self.r_top

    def __set_text(self, input_text='[ TEXT ]', font_size=24, text_color='white'):  # noqa: E501
        rtop_text = qtw.QLabel(text=input_text)
        rtop_text.setStyleSheet(f"""
            color: {text_color};
            font-size: {font_size};
            font-weight: bold;
            """)
        rtop_text.setAlignment(qtc.Qt.AlignCenter)
        return rtop_text

    def __set_toolbar_icon(self, filename):
        toolbar_icon = MediaWidgets().create_pushIcon(filename)
        toolbar_icon.setStyleSheet('border: None; margin: auto;')
        toolbar_icon.setFixedSize(40, 30)
        toolbar_icon.setIconSize(qtc.QSize(30, 30))
        return toolbar_icon

class RightMiddlePanel:
    """Handles the buttons in the right middle panel (rmp)."""

    def build_panel():
        """create Hbox panel to hold the buttons."""

        export_button = RightMiddlePanel.export_button()
        save_button = RightMiddlePanel.save_button()

        return [export_button, save_button]
        pass

    def export_button():
        """Create export button."""
        export_button = MediaWidgets().create_pushIcon("heart_icon.png")
        export_button.setFixedHeight(40)
        export_button.setFixedWidth(50)
        return export_button

    def save_button():
        """Create save button."""
        save_button = MediaWidgets().create_pushIcon("save_icon.png")
        save_button.setFixedHeight(40)
        save_button.setFixedWidth(50)
        return save_button

class RightBottomPanel:
    """Handles all views on the right bottom panel (rbp)."""

    def trending_page(recipe_name, diet_type, prep_time, ingredients_list):
        """Build the trending page onto the right bottom panel."""
        # creating left Widget with picture
        pic_widget = RightBottomPanel().left_parent("no_pic.png")

        # Creating right Widget label (Vbox layout)
        right_widget = RightBottomPanel().create_right_widget()

        recipe_label = RightBottomPanel().recipe_name_label(f"{recipe_name}")
        diet_type_label = RightBottomPanel().diet_type_label(f"{diet_type}")
        ingredients_label = RightBottomPanel().ingredients_label(f"{ingredients_list}")

        # Creating cooking icon and time widget
        cooking_time_pic = RightBottomPanel().cooking_time_pic("timer2.png")
        cooking_time_label = RightBottomPanel().cooking_time_label(f"{prep_time}")
        
        cooking_time = RightBottomPanel().cooking_time_widget()
        cooking_time.layout().addWidget(cooking_time_pic)
        cooking_time.layout().addWidget(cooking_time_label)

        # Adding widgets to the right Widget
        right_widget.layout().addWidget(recipe_label)
        right_widget.layout().addWidget(diet_type_label)
        right_widget.layout().addWidget(cooking_time)
        right_widget.layout().addWidget(ingredients_label)

        # Main parent Widget
        results = qtw.QWidget()
        results.setLayout(qtw.QHBoxLayout())
        results.layout().addWidget(pic_widget)
        results.layout().addWidget(right_widget)

        return results

    def search_results_page(recipe_name, diet_type, prep_time, ingredients_list):
        """Build the search results page on the right bottom panel (rbp)."""

        # creating left Widget with picture
        pic_widget = RightBottomPanel().left_parent("no_pic.png")

        # Creating right Widget label (Vbox layout)
        right_widget = RightBottomPanel().create_right_widget()

        recipe_label = RightBottomPanel().recipe_name_label(f"{recipe_name}")
        diet_type_label = RightBottomPanel().diet_type_label(f"{diet_type}")
        ingredients_label = RightBottomPanel().ingredients_label(f"{ingredients_list}")

        # Creating cooking icon and time widget
        cooking_time_pic = RightBottomPanel().cooking_time_pic("timer2.png")
        cooking_time_label = RightBottomPanel().cooking_time_label(f"{prep_time}")
        
        cooking_time = RightBottomPanel().cooking_time_widget()
        cooking_time.layout().addWidget(cooking_time_pic)
        cooking_time.layout().addWidget(cooking_time_label)

        # Adding widgets to the right Widget
        right_widget.layout().addWidget(recipe_label)
        right_widget.layout().addWidget(diet_type_label)
        right_widget.layout().addWidget(cooking_time)
        right_widget.layout().addWidget(ingredients_label)

        # Main parent Widget
        results = qtw.QWidget()
        results.setLayout(qtw.QHBoxLayout())
        results.layout().addWidget(pic_widget)
        results.layout().addWidget(right_widget)

        return results

    def favorites_page(recipe_name, diet_type, prep_time, ingredients_list):
        """Build the favorites page on the right bottom panel (rbp)."""
        # creating left Widget with picture
        pic_widget = RightBottomPanel().left_parent("no_pic.png")

        # Creating right Widget label (Vbox layout)
        right_widget = RightBottomPanel().create_right_widget()

        recipe_label = RightBottomPanel().recipe_name_label(f"{recipe_name}")
        diet_type_label = RightBottomPanel().diet_type_label(f"{diet_type}")
        ingredients_label = RightBottomPanel().ingredients_label(f"{ingredients_list}")

        # Creating cooking icon and time widget
        cooking_time_pic = RightBottomPanel().cooking_time_pic("timer2.png")
        cooking_time_label = RightBottomPanel().cooking_time_label(f"{prep_time}")
        
        cooking_time = RightBottomPanel().cooking_time_widget()
        cooking_time.layout().addWidget(cooking_time_pic)
        cooking_time.layout().addWidget(cooking_time_label)

        # Adding widgets to the right Widget
        right_widget.layout().addWidget(recipe_label)
        right_widget.layout().addWidget(diet_type_label)
        right_widget.layout().addWidget(cooking_time)
        right_widget.layout().addWidget(ingredients_label)

        # Main parent Widget
        results = qtw.QWidget()
        results.setLayout(qtw.QHBoxLayout())
        results.layout().addWidget(pic_widget)
        results.layout().addWidget(right_widget)

        return results

    def left_parent(self, picture):
        """Create Left most Widget to hold food picture."""
        pic_widget = qtw.QWidget()
        pic_widget.setLayout(qtw.QVBoxLayout())
        pic_widget.layout().setContentsMargins(0, 0, 0, 0)
        pic_widget.setFixedWidth(120)

        pic = MediaWidgets().create_img(picture)

        pic.setFixedWidth(120)
        pic.setFixedHeight(120)

        pic_widget.layout().addWidget(pic)
        pic_widget.setFixedHeight(120)

        pic_widget.layout().setAlignment(qtc.Qt.AlignTop)

        return pic_widget

    def create_right_widget(self):
        """Create right most Widget to hold multiple labels."""
        label_widget = qtw.QWidget()
        label_widget.setLayout(qtw.QVBoxLayout())
        label_widget.layout().setContentsMargins(0, 0, 0, 0)
        label_widget.layout().setSpacing(0)

        return label_widget

    def recipe_name_label(self, food_name):
        """Create recipe name label."""
        recipe_name = qtw.QLabel(f"{food_name}")
        recipe_name.setFixedHeight(40)
        recipe_name.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        
        return recipe_name

    def diet_type_label(self, diet_type):
        """Create diet type label."""

        if diet_type == "Vegan":
            diet_colour = "#32a852"
        elif diet_type == "Vegetarian":
            diet_colour = "#137d2c"
        elif diet_type == "Pescatarian":
            diet_colour = "#2a75a3"
        elif diet_type == "keto":
            diet_colour = "#d18436"
        else:
            diet_colour = "#8c0000" # remove later

        diet_type = qtw.QLabel(f"{diet_type}")
        diet_type.setFixedHeight(20)
        diet_type.setStyleSheet(f"color: {diet_colour}; font-size: 14px; font-weight: bold;")

        return diet_type

    def cooking_time_widget(self):
        """Create diet type label."""
        cooking_time = qtw.QWidget()
        cooking_time.setLayout(qtw.QHBoxLayout())
        cooking_time.layout().setSpacing(0)
        cooking_time.setFixedHeight(27)
        cooking_time.layout().setAlignment(qtc.Qt.AlignLeft)
        cooking_time.layout().setContentsMargins(0, 0, 0, 0)

        return cooking_time 

    def cooking_time_pic(self, picture):
        """Create timer icon."""
        timer_icon = MediaWidgets().create_imgWithScale(picture, 20, 20)
        timer_icon.setFixedWidth(25)

        return timer_icon

    def cooking_time_label(self, time):
        """Create label to hold cooking time."""
        cooking_time = qtw.QLabel(f"{time}")
        cooking_time.setFixedHeight(20)
        cooking_time.setStyleSheet("color: white; font-size: 8px; font-weight: bold;")

        return cooking_time

    def ingredients_label(self, ingredients):
        """Create label for ingredients list."""
        ingredients_list = qtw.QLabel(f"{ingredients}")
        ingredients_list.setStyleSheet("color: white; font-size: 12px; font-weight: bold;")
        ingredients_list.setAlignment(qtc.Qt.AlignTop)
        
        return ingredients_list
