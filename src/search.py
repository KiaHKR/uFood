import mysql.connector


class Search:


    mydb = None
    db_ingredients = [
        "ass",
        "tits",
        "fucking end me",
        "eewtrwea",
        "wadfwafwa",
        "fsafsdavaf",
        "feafcvaws",
        "hnvuies",
    ]

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "dbread",
            password = "6stooges",
            database = "ufood"
        ) 
        self.mycursor = self.mydb.cursor()
        pass

    def recipe_name_search(self, srch):
        self.mycursor.execute("SELECT recipes.name as 'Recipe name', recipes.cooking_time as 'Cooking time',GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets',GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE recipes.name LIKE '%%"+srch+"%%' Group by name")
        for x in self.mycursor:
            print(x)
        pass

    def ingredient_name_search(self):
        pass

    def cooking_time_search(self):
        pass