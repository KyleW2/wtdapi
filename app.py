from flask import Flask, render_template, request
from wordlist import WordList
from datetime import date

app = Flask(__name__)

words = WordList("words.csv")

@app.route("/", methods = ["GET"])
def index():
    return "<p>Word of the day API. Access through /api/</p>"

@app.route("/api/", methods = ["GET"])
def api():
    w = words.get_todays_word(date.today().day)
    return {"word": w.word, "definition": w.definition}


@app.route("/api/random", methods = ["GET"])
def api_random():
    w =  words.get_random_word()
    return {"word": w.word, "definition": w.definition}

@app.route("/game/practice", methods = ["GET"])
def game():
    w = words.get_random_word()
    return render_template("game.html", word = w)