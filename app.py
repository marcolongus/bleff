from flask import Flask, request, jsonify, redirect, url_for
from views import views 

#request, jsonify, render_template, redirect, views, url_for
#from contextlib import closing
#import sqlite3

app = Flask(__name__)
app.debug = True

app.register_blueprint(views, url_prefix="/")

@app.route('/post_definition', methods=['POST'])
def post_definition():
    definition = request.json.get('definition')
    print("Definition:\n")
    print(definition)
    print("\n\n\n")
    return redirect(url_for('views.lobby'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)










# @app.route('/post_definition', methods=['POST'])
# def post_definition():
#     definition = request.json.get('definition')
#     word = 'Mono' # This should be replaced with the word you want to insert

#     with closing(create_connection()) as connection:
#         cursor = connection.cursor()
#         cursor.execute("INSERT INTO words VALUES (?, ?)", (word, definition))
#         connection.commit()
#         cursor.execute("SELECT * FROM words WHERE word=?", (word,))
#         print((cursor.fetchall()))
#         # Process the results if needed
#     return redirect('/definition_received')

# @app.route('/definition_received') # Corrected spelling here
# def definition_received():
#     return render_template('waitingHall.html')
