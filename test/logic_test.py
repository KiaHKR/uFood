"""Logic unittest file."""

import unittest

from PyQt5.QtGui import QTextItem
from PyQt5.QtWidgets import QLabel, QWidgetItem
from pathlib import Path
import os

from src.bin import logic

# ctrl c-k
# ctsl k-u
class TestLogicClass(unittest.TestCase):
    """Tests Logic class."""

    def test_get_matching_ingredients(self):
        """Test getting the matching ingredients to search."""
        res = len(logic.Logic.get_matching_ingredients("mincemeat"))
        exp = 1
        self.assertEqual(res, exp)

    def test_ingr_selected(self):
        """Test adding and removing ingredients from the selected_ingredients list."""
        l = logic.Logic
        item = QLabel()
        item.setText("potatoes")
        l.add_ingr_selected(item)
        res = len(logic.selected_ingredients)
        self.assertEqual(res, 1)
        l.remove_ingr_selected(item)
        res2 = len(logic.selected_ingredients)
        self.assertEqual(res2, 0)

    def test_get_trending(self):
        """Test get trending."""
        res = len(logic.Logic.get_trending())
        self.assertEqual(res, 5)

    def test_get_ingredient_search(self):
        """Test getting ingredients from search."""
        l = logic.Logic
        item = QLabel()
        item.setText("potatoes")
        l.add_ingr_selected(item)
        res = len(l.get_ingredient_search(300))
        self.assertEqual(res, 3)
        l.remove_ingr_selected(item)

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
        home = str(Path.home())
        os.remove(home + "/Downloads/recipe.pdf")
