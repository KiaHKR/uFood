import mysql.connector


class Search:


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
        return_list = []
        self.mycursor.execute("SELECT recipes.name as 'Recipe name', recipes.cooking_time as 'Cooking time',GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets',GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', recipes.img_link as 'Image URL' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE recipes.name LIKE '%%"+srch+"%%' Group by name")
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def trending(self):
        return_list = []
        self.mycursor.execute("SELECT recipes.name as 'Recipe name', recipes.cooking_time as 'Cooking time',GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets',GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', recipes.img_link as 'Image URL' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id GROUP BY name ORDER BY times_accessed ASC")
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def ingredient_name_search(self, ing_list):
        ingred = ""
        return_list = []
        for x in ing_list[0:len(ing_list)-1]:
            ingred += "ingredients_has_recipes.ingredients_name = '" + x + "' or "
        ingred += " ingredients_has_recipes.ingredients_name = '" + ing_list[-1] + "'"    
        self.mycursor.execute("SELECT recipes.name as 'Recipe name', recipes.cooking_time as 'Cooking time', GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets', GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE "+ ingred +" GROUP BY name")
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def cooking_time_search(self, time):
        return_list = []
        self.mycursor.execute("SELECT recipes.name as 'Recipe name', GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets', recipes.cooking_time as 'Cooking time' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE cooking_time < '"+ time + "'  GROUP BY name;")
        for x in self.mycursor:
            return_list.append(x)
        return return_list

    def diet_type_filter(self, diet):
        return_list = []
        self.mycursor.execute("SELECT recipes.name as 'Recipe name', GROUP_CONCAT(ingredients_has_recipes.ingredients_name) as 'Ingredients', GROUP_CONCAT(DISTINCT recipes_has_diets.diets_name) as 'Diets', recipes.cooking_time as 'Cooking time' FROM recipes INNER JOIN recipes_has_diets ON recipes.id = recipes_has_diets.recipes_id INNER JOIN ingredients_has_recipes ON recipes.id = ingredients_has_recipes.recipes_id WHERE diets_name LIKE '"+diet+"' GROUP BY name;")
        for x in self.mycursor:
            return_list.append(x)
        return return_list

pe = Search()
x1 = pe.diet_type_filter("keto")
print(x1)