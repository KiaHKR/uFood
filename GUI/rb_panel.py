"""This class caters to all bottom panel events. It is a WIP."""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from random import randrange


class RightBottomPanel():
    """Returns relevant page settings for the right bottom panel."""

    def __init__(self, *args, **kwargs):
        """Build constructor."""
        pass

    def trending_page(self):
        """Build trending page."""
        pass

    def search_results_page(self):
        """Build search results page."""

        option = qtw.QWidget()

        self.create_recipe_label()

        self.create_diet_type_label()
        
        self.create_cooking_time()

        self.create_cooking_time_pic()

        self.create_ingredients_list()

        self.create_cooking_timer()

        self.cooking_timer.layout().addWidget(self.cooking_time_pic)
        self.cooking_timer.layout().addWidget(self.cooking_time)

        self.create_ingredient_label()

        self.ingredients_label.layout().addWidget(self.cooking_timer)
        self.ingredients_label.layout().addWidget(self.ingredients_list)
        self.ingredients_label.layout().setContentsMargins(0, 0, 0, 0)

        self.create_label_widget()
        self.label_widget.layout().addWidget(self.recipe_label)
        self.label_widget.layout().addWidget(self.diet_type_label)
        self.label_widget.layout().addWidget(self.ingredients_label)

        # pic_widget and label_widget get added to parent widget
        option.setLayout(qtw.QHBoxLayout())
        self.create_left_parent()
        option.layout().addWidget(self.pic_widget)
        option.layout().addWidget(self.label_widget)

        return option

    def favorite_page(self):
        """Build favorite page."""
        pass

    def create_left_parent(self):
        self.pic_widget = qtw.QWidget()
        self.pic_widget.setLayout(qtw.QVBoxLayout())
        self.pic_widget.layout().setContentsMargins(0, 0, 0, 0)

        picture = qtw.QLabel(
            pixmap=qtg.QPixmap("assets/test_asser.png").scaled(120, 120)
            )
        picture.setFixedWidth(120)
        picture.setFixedHeight(120)

        self.pic_widget.layout().addWidget(picture)
        self.pic_widget.setFixedWidth(120)

        self.pic_widget.layout().setAlignment(qtc.Qt.AlignTop)

    def create_label_widget(self):
        self.label_widget = qtw.QWidget()
        self.label_widget.setLayout(qtw.QVBoxLayout())
        self.label_widget.layout().setContentsMargins(0, 0, 0, 0)

    def create_recipe_label(self):
        self.recipe_label = qtw.QLabel("[FOOD NAME]")
        self.recipe_label.setFixedHeight(30)
        self.recipe_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")

    def create_diet_type_label(self):
        food_type_list = ["Vegan", "Vegetarian", "Pescatarian", "keto"]
        food_type = food_type_list[randrange(4)]
        if food_type == "Vegan":
            diet_colour = "#32a852"
        elif food_type == "Vegetarian":
            diet_colour = "#137d2c"
        elif food_type == "Pescatarian":
            diet_colour = "#2a75a3"
        elif food_type == "keto":
            diet_colour = "#d18436"
        self.diet_type_label = qtw.QLabel(f"{food_type}")
        self.diet_type_label.setFixedHeight(20)
        self.diet_type_label.setStyleSheet(f"color: {diet_colour}; font-size: 16px; font-weight: bold;")

    def create_ingredient_label(self):
        self.ingredients_label = qtw.QWidget()
        self.ingredients_label.setLayout(qtw.QVBoxLayout())

    def create_cooking_timer(self):
        self.cooking_timer = qtw.QWidget()
        self.cooking_timer.setLayout(qtw.QHBoxLayout())
        self.cooking_timer.layout().setSpacing(0)
        self.cooking_timer.layout().setAlignment(qtc.Qt.AlignLeft)
        self.cooking_timer.layout().setContentsMargins(0, 0, 0, 0)

    def create_cooking_time_pic(self):
        self.cooking_time_pic = qtw.QLabel(
            pixmap=qtg.QPixmap("assets/timer2.png").scaled(20, 20)
            )
        self.cooking_time_pic.setFixedWidth(25)

    def create_cooking_time(self):
        self.cooking_time = qtw.QLabel("[COOKING TIME]")
        self.cooking_time.setFixedHeight(20)
        self.cooking_time.setStyleSheet("color: white; font-size: 8px; font-weight: bold;")

    def create_ingredients_list(self):
        self.ingredients_list = qtw.QLabel("INGREDIENT LIST")
        self.ingredients_list.setStyleSheet("color: white; font-size: 12px; font-weight: bold;")