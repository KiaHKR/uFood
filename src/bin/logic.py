import pickle


class Logic:
    """Logic for the more complex actions."""

    def add_fav(self, id):
        Sync.fave_list.append(id)


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
