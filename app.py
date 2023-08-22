#TODO: rellamar presesnter a los script de .js
#TODO: ver como usar boostrap.

#==============================================
# IMPORTS
#==============================================
from flask import Flask, request, jsonify

from views import views 
from auth import auth

import sqlite3
from contextlib import closing

#==============================================
# CLASS
#==============================================
class DefinitionControler:
    def __init__(connection):
        self.connection = sqlite3.connect("dictionary.db")

    def insert_definition(self, word, definition):
        #TODO: Catchear exceptions.
        #TODO: RESOLVER LA LOGICA AQUI   
        self.connection.execute("INSERT INTO words VALUES (?, ?)", (word, definition))
        self.connection.commit()
        return None  
    
    def close(self):
        self.connection.close()

    def get_definitions(self, word):
        self.connection.execute("SELECT * FROM words WHERE word=?", (word,))
        print((self.connection.fetchall()))
        return None
#==============================================
# API
#==============================================
app = Flask(__name__)
app.debug = True

app.register_blueprint(views, url_prefix="/")

controller = DefinitionControler()

@app.route('/post_definition', methods=['GET', 'POST'])
def post_definition():
    #TODO resolver el mock
    definition = request.json.get('definition')
    controller.insert_deinition("mock_word", definition)
    controller.get_definitions("mock_word")
    return jsonify(status="definition received"), 200 


if __name__ == '__main__':
    app.run(debug=True, port=8000)



