from flask import Flask, render_template, request
from wordlist import WordList
from datetime import date

app = Flask(__name__)

dictionary = WordList("words.csv", 0, 3)
jeopardy = WordList("jeopardy.csv", 4, 2)

@app.route("/", methods = ["GET"])
def index():
    return "<p>Word of the day API. Access through /api/</p>"

@app.route("/api/", methods = ["GET"])
def api():
    w = dictionary.get_todays_word(date.today().day)
    return {"word": w.word, "definition": w.definition}


@app.route("/api/random", methods = ["GET"])
def api_random():
    w =  dictionary.get_random_word()
    return {"word": w.word, "definition": w.definition}

@app.route("/game/dictionary/practice", methods = ["GET"])
def dictionary_game():
    w = dictionary.get_random_word()
    return render_template("game.html", word = w)

@app.route("/game/jeopardy/practice", methods = ["GET"])
def jeopardy_game():
    w = jeopardy.get_random_word()
    return render_template("game.html", word = w)