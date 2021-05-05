"""Logic file for Logic and sync class."""
import pickle
from pathlib import Path
from PyPDF2 import PdfFileReader
from src.bin import query

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

    # https://realpython.com/creating-modifying-pdf/
    def __init__(self, name, instructions, source):
        """Creates a pdf with recipe info."""
        pdf_path = Path.home() / "Downloads" / "recipe.pdf"

        pdf_reader = PdfFileReader(str(pdf_path))

        with pdf_path.open(mode="w") as output_file:

            title = pdf_reader.documentInfo.title
            num_pages = pdf_reader.getNumPages()
            output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")

            for page in pdf_reader.pages:
                text = page.extractText()
                output_file.write(text)
