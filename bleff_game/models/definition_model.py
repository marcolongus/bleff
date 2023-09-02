import sqlite3


class DefinitionModel:

    @staticmethod
    def init_db():
        conn = sqlite3.connect('definitions.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS definitions (word TEXT, definition TEXT)')
        conn.commit()
        conn.close()

    @staticmethod
    def add_definition(word, definition):
        print(word, definition)
        conn = sqlite3.connect('definitions.db')
        c = conn.cursor()
        c.execute("INSERT INTO definitions (word, definition) VALUES (?, ?)", (word, definition))
        conn.commit()
        conn.close()
