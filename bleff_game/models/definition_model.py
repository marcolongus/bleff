import sqlite3

class DefinitionModel:
    """Logica de entidad y de base de datos
    
    Conecta a la base de datos y agrega las definiciones escritas 
    por el usuario. 

    """
    def __init__(self, database='definitions.db') -> None:
        self.database = database
        self.conn = sqlite3.connect(database)
    
    def verify_connectivity(self):
        ...

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def add_definition(self, word, definition):
        print(word, definition)
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO definitions (word, definition) VALUES (?, ?)", (word, definition))
        self.commit()
        cursor.close()
    





# import sqlite3


# class DefinitionModel:

#     @staticmethod
#     def init_db():
#         conn = sqlite3.connect('definitions.db')
#         c = conn.cursor()
#         c.execute('CREATE TABLE IF NOT EXISTS definitions (word TEXT, definition TEXT)')
#         conn.commit()
#         conn.close()

#     @staticmethod
#     def add_definition(word, definition):
#         print(word, definition)
#         conn = sqlite3.connect('definitions.db')
#         c = conn.cursor()
#         c.execute("INSERT INTO definitions (word, definition) VALUES (?, ?)", (word, definition))
#         conn.commit()
#         conn.close()
