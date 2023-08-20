import sqlite3

connection = sqlite3.connect("dictionary.db")

c = connection.cursor()

def create_table(c):
	c.execute("""CREATE TABLE words (
		word TEXT,
		definition TEXT
		)""")

c.execute("INSERT INTO words VALUES ('Mono', 'Mamifero peludo')")
c.execute("INSERT INTO words VALUES ('Mono', 'Bicho del monte')")
connection.commit()


c.execute("SELECT * FROM words WHERE word='Mono'")

#print((c.fetchone()))
print((c.fetchall()))



connection.commit()
connection.close()