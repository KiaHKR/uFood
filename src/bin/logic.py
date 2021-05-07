"""Logic file for Logic and sync class."""
import pickle
from fpdf import FPDF

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

    def remove_ingr_selected(ingr):
        """For removing the selected ingredient."""
        selected_ingredients.remove(ingr.text())

    def get_trending():
        """Returns list of top 5 trending from query."""
        return search_object.trending()[:5]

    def get_ingredient_search():
        """Returns list of recipes matching ingredients."""
        return search_object.ingredient_name_search(selected_ingredients)


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
    def __init__(self, name, ingred, instructions, source):
        """Creates a pdf with recipe info."""
        # Create an instance of the fpdf class
        pdf = FPDF()

        # Add a page
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        # Title
        # create a cell
        pdf.cell(100, 10, txt=name, ln=1, align="C")

        # Ingredients

        pdf.multi_cell(
            100,
            10,
            txt="Igredients: \n" + ingred,
            align="L",
        )

        # Instructions
        pdf.multi_cell(
            100,
            10,
            txt="Instructions: \n" + instructions,
            align="C",
        )

        # Source
        pdf.cell(200, 20, txt="Source", ln=1, align="C", link=source)

        # save the pdf with name .pdf
        home = str(Path.home())
        pdf.output(home + "/Downloads/" + name + ".pdf")  # or name + ".pdf"
