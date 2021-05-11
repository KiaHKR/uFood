"""Logic unittest file."""

import unittest

from PyQt5.QtWidgets import QLabel
from src.bin import logic


class TestLogicClass(unittest.TestCase):
    """Tests Logic class."""

    def test_get_matching_ingredients(self):
        """Test getting the matching ingredients to search."""
        res = len(logic.Logic.get_matching_ingredients("mincemeat"))
        exp = 1
        self.assertEqual(res, exp)

    def test_ingr_selected(self):
        """Test adding/removing ingredients from the selected_ingredients."""
        log = logic.Logic
        item = QLabel()
        item.setText("potatoes")
        log.add_ingr_selected(item)
        res = len(logic.selected_ingredients)
        self.assertEqual(res, 1)
        log.remove_ingr_selected(item)
        res2 = len(logic.selected_ingredients)
        self.assertEqual(res2, 0)

    def test_get_trending(self):
        """Test get trending."""
        res = len(logic.Logic.get_trending())
        self.assertEqual(res, 5)

    def test_get_ingredient_search(self):
        """Test getting ingredients from search."""
        log = logic.Logic
        item = QLabel()
        item.setText("potatoes")
        log.add_ingr_selected(item)
        res = len(log.get_ingredient_search(300))
        self.assertEqual(res, 3)
        log.remove_ingr_selected(item)

    # def test_name_search(self):
    #     """Test searching recipe by name."""
    #     l = logic.Logic
    #     item = QLabel()
    #     item.setText("pancakes")
    #     l.add_ingr_selected(item)
    #     res = len(l.name_search(item, 6000))
    #     self.assertEqual(res, 1)

    def test_max_cook_time(self):
        """Test get highest cook time."""
        res = logic.Logic.max_cook_time()
        self.assertEqual(res, 100)

    # Sync class testing
    def test_pickle(self):
        """Test all the pickle functions."""
        s = logic.Sync()
        s.add_favo(5)
        res = s.pickle_read()
        self.assertEqual(type(res), list)
        with self.assertRaises(FileNotFoundError):
            s.file = "shitttt"
            s.pickle_read()

    def test_add_fav(self):
        """Test adding soemthing to favorites."""
        self.assertTrue(logic.Logic().add_fav(2))

    def test_pdf(self):
        """Test the pdf feature."""
        self.assertEqual(
            type(
                logic.Pdf(
                    "chicken masala",
                    "chicken, tomato",
                    "instruction",
                    "google.com",
                )
            ),
            logic.Pdf,
        )
