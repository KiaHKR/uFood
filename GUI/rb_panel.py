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

        for _ in range(0, 20):
            rp_bottom = qtw.QWidget()
            rp_bottom.setStyleSheet(
                    """border: 2px solid purple;
                    color: white;
                    font-size: 20px;"""
                )
            rp_bottom.setLayout(qtw.QVBoxLayout())
            rp_bottom.layout().addWidget(qtw.QLabel(text="this panel will change")) 

        return rp_bottom

    def search_results_page(self):
        """Build search results page."""

        option = qtw.QWidget()

        # creating left and right Widgets
        pic_widget = qtw.QWidget()
        pic_widget.setLayout(qtw.QVBoxLayout())

        picture = qtw.QLabel(
            pixmap=qtg.QPixmap("assets/test_asser.png").scaled(120, 120)
            )
        picture.setFixedWidth(120)
        picture.setFixedHeight(120)  

        pic_widget.layout().addWidget(picture) 
        pic_widget.setFixedWidth(125)

        pic_widget.layout().setAlignment(qtc.Qt.AlignTop)  
        pic_widget.layout().setSpacing(0)  

        # unecessary bit added for showcase

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

        # Left widget
        label_widget = qtw.QWidget()
        label_widget.setLayout(qtw.QVBoxLayout())

        recipe_label = qtw.QLabel("[FOOD NAME]")
        recipe_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        diet_type_label = qtw.QLabel(f"{food_type}")
        diet_type_label.setStyleSheet(f"color: {diet_colour}; font-size: 16px; font-weight: bold;")
        
        
        ingredients_label = qtw.QWidget()
        ingredients_label.setLayout(qtw.QVBoxLayout())


        cooking_timer = qtw.QWidget()
        cooking_timer.setLayout(qtw.QHBoxLayout())

        cooking_time_pic = qtw.QLabel(
            pixmap=qtg.QPixmap("assets/timer.png").scaled(15, 15)
            )
        cooking_time_pic.setFixedWidth(20)

        cooking_time = qtw.QLabel("[COOKING TIME]")
        cooking_time.setFixedHeight(20)
        cooking_time.setStyleSheet("color: white; font-size: 8px; font-weight: bold;")

        ingredients_list = qtw.QLabel("INGREDIENT LIST")
        ingredients_list.setStyleSheet("color: white; font-size: 10px; font-weight: bold;")

        cooking_timer.layout().addWidget(cooking_time_pic)
        cooking_timer.layout().addWidget(cooking_time)
        cooking_timer.layout().setSpacing(0)
        cooking_timer.layout().setAlignment(qtc.Qt.AlignLeft)
        cooking_timer.layout().setContentsMargins(0, 0, 0, 0)

        ingredients_label.layout().addWidget(cooking_timer)
        ingredients_label.layout().addWidget(ingredients_list)
        ingredients_label.setFixedHeight(100)
        ingredients_label.layout().setContentsMargins(5, 0, 0, 0)

        label_widget.layout().addWidget(recipe_label)
        label_widget.layout().addWidget(diet_type_label)
        label_widget.layout().addWidget(ingredients_label)

        # this is where the two main Widgets get added
        option.setLayout(qtw.QHBoxLayout())
        option.layout().addWidget(pic_widget)
        option.layout().addWidget(label_widget)

        return option

    def favorite_page(self):
        """Build favorite page."""
        pass
