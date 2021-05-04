import pickle
from src.bin import query

selected_ingredients = []
search_object = query.Search()

<<<<<<< HEAD
class Logic:
    """Logic for the more complex actions."""

=======

class Logic:
>>>>>>> 1615216565ec773d3bef2f92fdd4cb0961a37c04
    def add_fav(self, id):
        Sync.fave_list.append(id)

    def get_matching_ingredients(search):
        master_ingr = search_object.get_ingredient(search)

        ingr_list = []

        for i in master_ingr:
            if search in i and i not in selected_ingredients:
                ingr_list.append(i)

<<<<<<< HEAD
=======
        return ingr_list

    def add_ingr_selected(ingr):
        selected_ingredients.append(ingr.text())


>>>>>>> 1615216565ec773d3bef2f92fdd4cb0961a37c04
class Sync:
    """Dynchronization for objects when writing to/reading from."""

    file = "src/interface/assets/pickle.pickle"
    fav_list = []

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
