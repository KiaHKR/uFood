import mysql.connector

class Write_queries:
    """ADMIN MODE ONLY"""

    def __init__(self):
        """Init function."""
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "dbwrite",
            password = "reality",
            database = "ufood"
        )

    def write(statement):
        self.mydb(statement)
