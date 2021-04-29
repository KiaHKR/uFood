from GUI import flow_layout as flow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class IngredientWidget:
    """Class for handling visualisation of selected ingredients."""

    def __init__(self):
        """Creates basic layout as instance var."""
        self.ingredient_widget = qtw.QWidget()
        self.ingredient_widget.setStyleSheet("border: 2px solid red")
        self.ingredient_widget.setLayout(flow.FlowLayout())

    def update_ingredients(self, selected_ingredients):
        """Adds the UI element of specified ingredient."""
        for i in selected_ingredients:
            widget = qtw.QWidget()
            widget.setLayout(qtw.QHBoxLayout())
            widget.setStyleSheet("border: 1px solid white")

            label = qtw.QLabel()
            label.setStyleSheet("color: white; font-size: 14px")
            print(i)
            label.setText(i)
            label.setFixedSize(len(i) * 7, 15)

            widget.layout().addWidget(label)
            self.ingredient_widget.layout().addWidget(widget)
