"""Query unittest file."""


import unittest
from src.bin import query


class TestQueryClass(unittest.TestCase):
    """Tests Query class."""

    def test_create_connection(self):
        """Tests object and connection creation."""
        connection = query.Search()
        res = connection
        self.assertIsInstance(res, query.Search)

    def test_recipe_name_search(self):
        """Tests the recipe search by name."""
        connection = query.Search()
        res = len(connection.recipe_name_search("Omlette"))
        exp = 1
        self.assertEqual(res, exp)

    def test_trending(self):
        """Test trending recipe search."""
        connection = query.Search()
        res = connection.trending()[1][0]
        exp = "Basic Omlette"
        self.assertEqual(res, exp)

    def test_ingredient_name_search(self):
        """Tests the search of recipe by ingredient."""
        connection = query.Search()
        res = len(connection.ingredient_name_search(["eggs"]))
        exp = 16
        self.assertEqual(res, exp)

    def test_cooking_time_search(self):
        """Test the search of recipes by maximum cooking time."""
        connection = query.Search()
        res = len(connection.cooking_time_search("00:10:00"))
        exp = 2
        self.assertEqual(res, exp)

    def test_diet_type_filter(self):
        """Test the search for recipes by diet type."""
        connection = query.Search()
        res = len(connection.diet_type_filter("paleo"))
        exp = 2
        self.assertEqual(res, exp)

    def test_get_instructions(self):
        """Test the search for instructions with recipeID."""
        connection = query.Search()
        res = connection.get_instructions("1")
        self.assertIn("STEP 1", res)

    def test_get_ingredients(self):
        """Test to get ingredients with part of ingredient name."""
        connection = query.Search()
        res = len(connection.get_ingredient("egg"))
        exp = 1
        self.assertEqual(res, exp)

    def test_get_export_info(self):
        """Test receive information to export."""
        connection = query.Search()
        qry = connection.get_export_info("1")
        res = len(qry)
        exp = 4
        self.assertEqual(res, exp)

    def test_recipe_id_search(self):
        """Test recipe search by ID."""
        connection = query.Search()
        res = len(connection.recipe_id_search("1"))
        self.assertEqual(1, res)
