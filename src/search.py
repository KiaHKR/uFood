import mysql.connector


class Search:

    mydb = None

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost", user="root", password="Regnskov123!"
        )

    def recipe_name_search(self):
        pass

    def ingredient_name_search(self):
        pass

    def cooking_time_search(self):
        pass