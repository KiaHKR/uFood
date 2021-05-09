"""Query file for search class."""
import mysql.connector


class Search:
    """Search class for Qureries needed to search for recipes."""

    def __init__(self):
        """Is constructor of search class."""
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="dbread",
            password="6stooges",
            database="ufood",
        )
        self.mycursor = self.mydb.cursor()

    def recipe_id_search(self, srch):
        """For searching recipe names."""
        return_list = []
        self.mycursor.execute(
            "SELECT recipes.name as 'Recipe name', recipes.cooking_time as 'Cooking time',GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets',GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', id as 'Recipe ID' ,recipes.img_link as 'Image URL' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE recipes.id ="
            + srch
            + " Group by name"
        )
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def recipe_name_search(self, srch):
        """For searching recipe names."""
        return_list = []
        self.mycursor.execute(
            "SELECT recipes.name as 'Recipe name', recipes.cooking_time as 'Cooking time',GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets',GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', id as 'Recipe ID' ,recipes.img_link as 'Image URL' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE recipes.name LIKE '%%"
            + srch
            + "%%' Group by name;"
        )
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def trending(self):
        """For finding trending recipes."""
        return_list = []
        self.mycursor.execute(
            "SELECT recipes.name as 'Recipe name', recipes.cooking_time as 'Cooking time', GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets', GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', id as 'Recipe ID' ,recipes.img_link as 'Image URL' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id GROUP BY name ORDER BY times_accessed ASC;"
        )
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def ingredient_name_search(self, ing_list):
        """For searching ingredients."""
        ingredient_list = []
        id_list = []
        if len(ing_list) == 1:
            ingred = "SELECT recipes.id FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE ingredients_has_recipes.recipes_id IN (SELECT recipes.id as 'ID' FROM recipes INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE ingredients_name = '"+ing_list[0]+"') GROUP BY ID"
        else:
            ingred = "SELECT recipes.id FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE ingredients_has_recipes.recipes_id IN (SELECT recipes.id as 'ID' FROM recipes INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE ingredients_name = '"+ing_list[0]+"') " 
            for x in ing_list[1:]:
                ingred = ingred + " AND ingredients_has_recipes.recipes_id IN (SELECT recipes.id as 'ID' FROM recipes INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE ingredients_name = '"+x+"') "
                ingred = ingred +" GROUP BY ID" 
        self.mycursor.execute(ingred)
        for id in self.mycursor:
            id_list.append(str(id[0]))       
        for id in id_list:
            self.mycursor.execute("SELECT recipes.name as 'Recipe name', recipes.cooking_time as 'Cooking time', GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets', GROUP_CONCAT(DISTINCT ingredients_has_recipes.ingredients_name) as 'Ingredients', id as 'Recipe ID' ,recipes.img_link as 'Image URL' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE ingredients_has_recipes.recipes_id = '"+id+"'")
            for yo in self.mycursor:
                a= yo[3]
                b=""
                for x in ing_list:
                    if x in a:
                        a = a.replace(x+",", "")
                        b += x+", "
                ingredient_list.append((yo[0],yo[1], yo[2], a, yo[4], yo[5], b))
        return ingredient_list

    def cooking_time_search(self, time):
        """For searching recipes by cooking time."""
        return_list = []
        self.mycursor.execute(
            "SELECT recipes.name as 'Recipe name', GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets', recipes.cooking_time as 'Cooking time', id as 'Recipe ID' ,recipes.img_link as 'Image URL' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE cooking_time < '"
            + time
            + "'  GROUP BY name;"
        )
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def diet_type_filter(self, diet):
        """For searching by diet types."""
        return_list = []
        self.mycursor.execute(
            "SELECT recipes.name as 'Recipe name', GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets', recipes.cooking_time as 'Cooking time', id as 'Recipe ID' ,recipes.img_link as 'Image URL' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE diets_name LIKE '"
            + diet
            + "' GROUP BY name;"
        )
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def get_instructions(self, recipeid):
        """For getting instructions of a recipe."""
        self.mycursor.execute(
            "SELECT instructions FROM recipes WHERE id = '" + recipeid + "';"
        )
        for x in self.mycursor:
            instr = x[0]
        return instr.replace("$", "\n")

    def get_ingredient(self, ingredient):
        """For getting the ingredients of a recipe."""
        return_list = []
        self.mycursor.execute(
            "SELECT name FROM ingredients WHERE name LIKE '"
            + ingredient
            + "%' or name LIKE '% "
            + ingredient
            + "%';"
        )
        for x in self.mycursor:
            for y in x:
                return_list.append(y)
        return return_list

    def get_export_info(self, recipeid):
        """Retrieves information about a (selected) recipe with an id. To later save."""
        self.mycursor.execute(
            "SELECT recipes.name, GROUP_CONCAT(CONCAT_WS(' '"
            ", ingredients_has_recipes.amount, "
            + "ingredients_has_recipes.measurements_name, "
            + "ingredients_has_recipes.ingredients_name) SEPARATOR '@')as 'Ingredients', "
            + "recipes.instructions, "
            + "recipes.source "
            + "FROM recipes "
            + "INNER JOIN ingredients_has_recipes "
            + "ON recipes.id = ingredients_has_recipes.recipes_id "
            + "WHERE recipes.id = '" + recipeid + "';"
        )
        for x in self.mycursor:
            name = x[0]
            ingred = x[1]
            instr = x[2]
            source = x[3]
        return (
            name,
            ingred.replace("@", "\n"),
            instr.replace("$", "\n"),
            source,
        )

