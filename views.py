from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
	my_word = "libertario"
	return render_template("main.html", word=my_word)

@views.route("/lobby")
def lobby():
	return render_template("lobby.html")