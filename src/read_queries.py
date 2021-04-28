import mysql.connector

class Read_queries:
    """COMMANDS TO READ FROM DB"""

    def __init__(self):
        """Init function."""
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "dbread",
            password = "6stooges",
            database = "ufood"
        )

    def read(field, table):
        res = self.mydb("SELECT "+field+"from "+ table)
        for x in res:
            print(x)