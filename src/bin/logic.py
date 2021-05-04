import pickle
from PyQt5 import QtCore

from PyQt5.QtWidgets import QVBoxLayout, QWidget
from src.bin import query

selected_ingredients = []
search_object = query.Search()


class Logic:
    """Logic for the more complex actions."""

    def add_fav(self, id):
        """Adds a favorite to pickle."""
        Sync.add_fav(id)

    def get_matching_ingredients(search):
        master_ingr = search_object.get_ingredient(search)

        ingr_list = []

        for i in master_ingr:
            if search in i and i not in selected_ingredients:
                ingr_list.append(i)

        return ingr_list

    def add_ingr_selected(ingr):
        selected_ingredients.append(ingr.text())

    def generate_recipe_cards(result_list):
        result_box = QWidget()
        result_box.setLayout(QVBoxLayout())
        result_box.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)


class Sync:
    """Dynchronization for objects when writing to/reading from."""

    def __init__(self):
        """Initializes by reading and saving the current pickle in a list."""
        self.file = "src/interface/assets/pickle.pickle"
        self.fav_list = []
        self.pickle_read()

    def add_fav(self, id):
        """Add new item to a list and renew pickle."""
        self.fav_list.append(id)
        self.pickle_write()

    def pickle_write(self):
        """Write to bin."""
        with open(self.file, "wb") as file:
            pickle.dump(self.fav_list, file)

    def pickle_read(self):
        """Read and initiates from bin."""
        with open(self.file, "rb") as file:
            self.fav_list = pickle.load(file)
            return (
                self.fav_list
            )  # send the list of fav id's to some class ehhee
