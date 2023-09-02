import sqlite3

# 

class GameModel:
    """ Logica de base de datos relacionada a la partida

        Si no existe la table games, la crea. 
    """

    @staticmethod
    def init_db():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS games (name TEXT)')
        conn.commit()
        conn.close()

    @staticmethod
    def create_game(name):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO games (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
