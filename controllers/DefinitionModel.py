import sqlite3
from contextlib import closing

class DefinitionModel:
    def __init__(self):
        self.connection = sqlite3.connect("dictionary.db")

    def insert_definition(self, word, definition):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute("INSERT INTO words VALUES (?, ?)", (word, definition))
            self.connection.commit()

    def close(self):
        self.connection.close()
