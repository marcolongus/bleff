from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
	my_word = "COSO"
	return render_template("main.html", word=my_word)

@views.route("/lobby/")
def lobby():
	return render_template("lobby.html")

# @views.route('/post_definition', methods=['GET', 'POST'])
# def post_definition():
#     definition = request.json.get('definition')
#     print("\nMESSAGE SENDED:", definition)
#     print("\n")
#     return redirect('/lobby/')
