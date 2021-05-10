"""Logic unittest file."""

import pickle
from fpdf import FPDF
import unittest
import src.bin.logic as logic


class TestLogicClass(unittest.TestCase):
    """Tests Logic class."""

    def test_get_matching_ingredients(self):
        """Tests getting the matching ingredients to search."""
        l = logic.Logic()
        res = len(l.get_matching_ingredients("mincemeat"))
        exp = 5
        self.assertEqual(res, exp)