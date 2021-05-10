"""File for Logic and sync class."""
import pickle
from fpdf import FPDF

from src.bin import query
import src.interface.root as root
from pathlib import Path

selected_ingredients = []
search_object = query.Search()


class Logic:
    """Logic for the more complex actions."""

    def add_fav(self, id):
        """For adding a favorite to pickle."""
        s = Sync()
        s.add_favo(id)
        return True

    def get_matching_ingredients(search):
        """For getting matching ingredients to search."""
        master_ingr = search_object.get_ingredient(search.lower())

        ingr_list = []

        for i in master_ingr:
            if search.lower() in i and i not in selected_ingredients:
                ingr_list.append(i)

        return ingr_list

    def add_ingr_selected(ingr):
        """For adding the selected ingredients."""
        selected_ingredients.append(ingr.text())

    def remove_ingr_selected(ingr):
        """For removing the selected ingredient."""
        selected_ingredients.remove(ingr.text())

    def get_trending():
        """Return list of top 5 trending from query."""
        return list(reversed(search_object.trending()[-5:]))

    def get_favorites():
        """Returns the recipes saved to favorites."""
        fave_id_list = Sync().pickle_read()
        recipe_list = []
        for i in fave_id_list:
            result = query.Search().search_for_fav(i)
            recipe_list.append(result[0])
        return recipe_list

    def get_ingredient_search(time_value):
        """Return list of recipes matching ingredients."""
        result_list = []
        return_list = search_object.ingredient_name_search(
            selected_ingredients
        )

        for i in return_list:
            time = int(str(i[1]).split(":")[0]) * 60 + int(
                str(i[1]).split(":")[1]
            )
            if time <= time_value:
                result_list.append(i)

        return result_list

    def name_search(search, time_value):
        """Search by recipe name, applies time and selected ingr."""
        return_list = []
        result_list = []

        if len(selected_ingredients) > 0:
            root.Controller.delete_recipe_cards()
            result_list = Logic.get_ingredient_search(time_value)
        elif search == "" or search == " ":
            return None
        elif search is None:
            root.Controller.delete_recipe_cards()
            result_list = query.Search().recipe_name_search("")
        else:
            root.Controller.delete_recipe_cards()
            result_list = query.Search().recipe_name_search("")

        for i in result_list:
            time = int(str(i[1]).split(":")[0]) * 60 + int(
                str(i[1]).split(":")[1]
            )

            if search is not None:
                if search.lower() in i[0].lower() and time <= time_value:
                    return_list.append(i)
            elif search is None and time <= time_value:
                return_list.append(i)

        return return_list

    def max_cook_time():
        """Return the highest cook time of all recipes."""
        unformated_time = str(search_object.get_max_cooking_time())
        time_minutes = int(unformated_time.split(":")[0]) * 60 + int(
            unformated_time.split(":")[1]
        )
        return time_minutes


class Sync:
    """Dynchronization for objects when writing to/reading from."""

    def __init__(self):
        """Read the current pickle in a list."""
        self.file = "src/interface/assets/pickle.pickle"
        self.fav_list = []
        try:
            self.pickle_read()
        except FileNotFoundError:
            self.pickle_write()

    def add_favo(self, id):
        """Add new item to a list and renew pickle."""
        if id in self.fav_list:
            self.fav_list.remove(id)
            self.pickle_write()
        elif id not in self.fav_list:
            self.fav_list.append(id)
            self.pickle_write()

    def pickle_write(self):
        """Write to bin."""
        with open(self.file, "wb") as file:
            pickle.dump(self.fav_list, file)

    def pickle_read(self):
        """Read from pickle file."""
        try:
            with open(self.file, "rb") as file:
                self.fav_list = pickle.load(file)
                return self.fav_list
        except FileNotFoundError as error:
            raise FileNotFoundError from error


class Pdf:
    """Creating a pdf od a recipe."""

    # https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/
    def __init__(self, name, ingred, instructions, source):
        """Create a pdf with recipe info."""
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
            txt="Ingredients: \n" + ingred,
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
        pdf.output(home + "/Downloads/" + name + ".pdf")
