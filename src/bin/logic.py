"""File for Logic and sync class."""
import os
import pickle
from PyQt5.QtGui import QIcon
from fpdf import FPDF

from src.bin import query
import src.interface.root as root
from PyQt5 import QtWidgets as qtw

selected_ingredients = []
search_object = query.Search()


class Logic:
    """Logic for the more complex actions."""

    def add_fav(self, id):
        """For adding a favorite to pickle."""
        s = Sync()
        if id not in Sync.fav_list:
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
        """Return the recipes saved to favorites."""
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
    """Synchronization for objects when writing to/reading from."""

    _export_path = "uFridge/"
    fav_list = []

    def __init__(self):
        """Read the current pickle in a list."""
        self.file = Sync._export_path + "favorites.pickle"

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
        if os.path.exists(self._export_path) is False:
            Sync.__pickle_setDownloadPath()
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

    def __pickle_setDownloadPath():
        """Set a download path for recipes/exports."""
        if os.path.exists(Sync._export_path) is False:
            os.mkdir(Sync._export_path)
        if os.path.exists(Sync._export_path + "My Exports") is False:
            os.mkdir(Sync._export_path + "My Exports")
        with open(Sync._export_path + "config.pickle", "wb") as f:
            pickle.dump(Sync._export_path, f)

    def pickle_getDownloadPath():
        """Retreive download path"""
        try:
            with open(Sync._export_path + "config.pickle", "rb") as f:
                content = pickle.load(f)
            return content
        except FileNotFoundError:
            Sync.__pickle_setDownloadPath()
            Sync.pickle_getDownloadPath()  # recursion

    def __rm_config():
        """Remove the existing config file."""
        if os.path.exists(Sync._export_path):
            os.remove("config.pickle")

    def adjust_downloadPath(path):
        """Adjust the download path."""
        Sync.__rm_config()
        Sync._export_path = path
        Sync.__pickle_setDownloadPath()

    def export_favorites():
        """Export favorites currently in list."""
        path = Sync.pickle_getDownloadPath()
        recipes_to_write = []
        with open(path + "favorites.pickle", "rb") as fav:
            contents = pickle.load(fav)
            for r in contents:
                recipes_to_write.append(r)
        with open(path + "My Exports/favorites_export.txt", "w") as f:
            for recipe in recipes_to_write:
                recipe_obj = query.Search().recipe_id_search(recipe)
                recipe_name = recipe_obj[0][0]
                f.write(recipe_name + "\n")
        msg = qtw.QMessageBox()
        msg.setWindowTitle("Success!")
        icon = QIcon("src/interface/assets/validation.png")

        msg.setWindowIcon(icon)
        msg.setText(
            f"Export successful to your '{Sync._export_path[:-1]}/My Exports' folder."
        )
        msg.exec_()

    def sync_to_fav(filepath):
        """Takes the import filepath and calculate the ids, then store to favs."""
        with open(filepath, "r") as import_file:
            content = import_file.read().split("\n")
            if content[0] != "":
                content = content[:-1]
                for i in range(0, len(content)):
                    recipe_tuple = query.Search().recipe_name_search(
                        content[i]
                    )
                    id = str(recipe_tuple[0][4])
                    Sync().add_unique_to_fav(id)
            msg = qtw.QMessageBox()
            msg.setWindowTitle("Success!")
            icon = QIcon("src/interface/assets/validation.png")
            msg.setWindowIcon(icon)
            msg.setText(f"Favorites successfully imported!")
            msg.exec_()

    def add_unique_to_fav(self, id):
        if id not in self.fav_list:
            self.fav_list.append(id)
            self.pickle_write()


class Pdf:
    """Creating a pdf of a recipe."""

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
        if os.path.exists(Sync._export_path + "Recipes/") is False:
            os.mkdir(Sync._export_path + "Recipes/")
        pdf.output(Sync._export_path + "Recipes/" f"{name}.pdf")

        # informative box
        msg = qtw.QMessageBox()
        msg.setWindowTitle("Info")
        msg.setWindowIcon(QIcon("src/interface/assets/validation.png"))
        msg.setText(
            f"A pdf has successfully been downloaded to your {Sync._export_path[:-1]} folder."
        )
        msg.exec_()
