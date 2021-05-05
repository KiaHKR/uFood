"""Logic file for Logic and sync class."""
import pickle
<<<<<<< HEAD
from fpdf import FPDF
=======
from PyQt5 import QtCore

from PyQt5.QtWidgets import QVBoxLayout, QWidget
>>>>>>> dev_lasse
from src.bin import query
from pathlib import Path

selected_ingredients = []
search_object = query.Search()


class Logic:
    """Logic for the more complex actions."""

    def add_fav(self, id):
        """For adding a favorite to pickle."""
        Sync.add_fav(id)

    def get_matching_ingredients(search):
        """For getting matching ingredients to search."""
        master_ingr = search_object.get_ingredient(search)

        ingr_list = []

        for i in master_ingr:
            if search in i and i not in selected_ingredients:
                ingr_list.append(i)

        return ingr_list

    def add_ingr_selected(ingr):
        """For adding the selected ingredients."""
        selected_ingredients.append(ingr.text())

    def generate_recipe_cards(result_list):
        result_box = QWidget()
        result_box.setLayout(QVBoxLayout())
        result_box.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)


class Sync:
    """Dynchronization for objects when writing to/reading from."""

    def __init__(self):
        """For initializing by reading and saving the current pickle in a list."""
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


class Pdf:
    """Creating a pdf od a recipe."""

    # https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/
    def __init__(self, name, instructions, source):
        """Creates a pdf with recipe info."""
        # Create an instance of the fpdf class
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=14)

        # create a cell
        pdf.cell(100, 10, txt=name, ln=1, align="C")

        # add another cell
        pdf.multi_cell(
            100,
            10,
            txt="Instructions: \n" + instructions,
            align="C",
        )

        pdf.cell(200, 20, txt=source, ln=2, align="C")

        # save the pdf with name .pdf
        home = str(Path.home())
        pdf.output(home + "/Downloads/recipe.pdf")  # or name + ".pdf"
