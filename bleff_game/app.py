import sqlite3
from flask import Flask, render_template, request, jsonify

from controllers.game_controller import GameController
from controllers.definition_controller import DefinitionController

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('main.html')


@app.route('/<game_name>')
def game_view(game_name):
    word = "LIBERTAD"
    return render_template('definition_input.html', game_name=game_name, word=word)

@app.route('/submit_definition', methods=['POST'])
def submit_definition():
    data = request.json
    word = data['word']
    definition = data['definition']
    print(word, definition)
    controller = DefinitionController()
    controller.save_definition(word, definition)
    return jsonify({'status': 'success'})



@app.route('/create_game', methods=['POST'])
def create_game():
    data = request.json
    name = data['name']
    controller = GameController(name)
    controller.create_game()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    # Initialize SQLite database if necessary
    conn = sqlite3.connect('definitions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS definitions (word TEXT, definition TEXT)''')
    conn.commit()
    conn.close()

    app.run(debug=True)
