#TODO: rellamar presesnter a los script de .js
#TODO: ver como usar boostrap.

#==============================================
# IMPORTS
#==============================================
import sys

sys.path.insert(1, "controllers")
sys.path.insert(2, "models")

from flask import Flask, request, jsonify

from views import views 
from auth import auth

from DefinitionController import DefinitionController

#==============================================
# API
#==============================================
app = Flask(__name__)
app.debug = True

app.register_blueprint(views, url_prefix="/")

controller = DefinitionController()

@app.route('/post_definition', methods=['GET', 'POST'])
def post_definition():
    #TODO resolver el mock
    definition = request.json.get('definition')
    word = request.json.get('word')
    controller.insert_definition(word, definition)
    #controller.get_definitions(word)
    return jsonify(status="definition received"), 200 


if __name__ == '__main__':
    app.run(debug=True, port=8000)



