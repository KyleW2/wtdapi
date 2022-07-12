from flask import Flask, render_template, request
from qalist import WordList
from datetime import date
from requests import get

app = Flask(__name__)
IP = get('https://api.ipify.org').content.decode('utf8')

dictionary = WordList("data/words.csv", 0, 3)
songs = WordList("data/songs.csv", 1, 0)

@app.route("/", methods = ["GET"])
def index():
    return "<p>Word of the day API. Access through /api/</p>"

@app.route("/api/", methods = ["GET"])
def api():
    w = dictionary.get_todays_word(date.today().day)
    return {"word": w.word, "definition": w.definition}

@app.route("/api/dictionary/random", methods = ["GET"])
def api_dictionary_random():
    w =  dictionary.get_random_word()
    return {"word": w.word, "definition": w.definition}

@app.route("/game/dictionary/practice", methods = ["GET"])
def dictionary_game():
    w = dictionary.get_random_word()
    return render_template("dictionary.html", word = w)

@app.route("/game/songs/practice", methods = ["GET"])
def songs_game():
    w = songs.get_random_word()
    return render_template("songs.html", word = w)