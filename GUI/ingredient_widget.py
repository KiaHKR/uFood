from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class IngredientWidget:
    """Class for handling visualisation of selected ingredients."""

    def __init__(self):
        """Creates basic layout as instance var."""
        self.ingredient_widget = qtw.QWidget()
        self.ingredient_widget.setStyleSheet("border: 2px solid red")
        self.ingredient_widget.setLayout(qtw.QVBoxLayout())
        self.hbox = qtw.QHBoxLayout()

    def add_ingredient(self, ingredient):
        """Adds the UI element of specified ingredient."""
        ingredient_label = self.create_ingredient(ingredient)

    def remove_ingredient(self, ingredient):
        """Removes the UI element of specified ingredient."""
        pass

    def create_ingredient(self, name):
        """Generates UI element for specified ingredient."""
        widget = qtw.QWidget()
        widget.setLayout(qtw.QHBoxLayout())
        label = qtw.QLabel()
        label.setText(name)
        label.setStyleSheet(
            "border: 1px white; font-size: 14px; color: white;"
        )
        label.setFixedSize(len(name) * 7, 14)
        widget.setFixedSize(label.width() + 40, 35)
        widget.layout().addWidget(label)
        widget.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignVCenter)
        widget.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignLeft)
        return widget
