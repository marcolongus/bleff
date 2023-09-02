import sqlite3

class DefinitionModel:
    """Logica de entidad y de base de datos
    
    Conecta a la base de datos y agrega las definiciones escritas 
    por el usuario. 

    """
    def __init__(self, database='definitions.db') -> None:
        self.database = database
        
    def add_definition(self, word, definition):
        print(word, definition)
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO definitions (word, definition) VALUES (?, ?)", (word, definition))
        connection.commit()
        connection.close()
    





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
