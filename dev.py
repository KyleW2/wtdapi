from flask import Flask, render_template, request
from qalist import QAList
from datetime import date

app = Flask(__name__)
IP = "http://127.0.0.1:5000"

dictionary = QAList("data/words.csv", 3, 0)
songs = QAList("data/songs.csv", 0, 1)

@app.route("/", methods = ["GET"])
def index():
    return "<p>Word of the day API. Access through /api/</p>"

# API
# Dictionary
@app.route("/api/dictionary/random", methods = ["GET"])
def api_dictionary_random():
    w =  dictionary.get_random_pair()
    return {"answer": w.answer, "question": w.question}

@app.route("/api/dictionary/daily", methods = ["GET"])
def api_dictionary_daily():
    w = dictionary.get_todays_pair(date.today().day)
    return {"answer": w.answer, "question": w.question}

# Songs
@app.route("/api/songs/random", methods = ["GET"])
def api_songs_random():
    w = songs.get_random_pair()
    return {"answer": w.answer, "question": w.question}

@app.route("/api/songs/daily", methods = ["GET"])
def songs_game():
    w = songs.get_todays_pair(date.today().day)
    return {"answer": w.answer, "question": w.question}

# GAME
# Dictionary
@app.route("/game/dictionary/random", methods = ["GET"])
def game_dictionary_random():
    w = dictionary.get_random_pair()
    return render_template("dictionary/page.html", word = w)

@app.route("/game/dictionary/daily", methods = ["GET"])
def game_dictionary_daily():
    w = dictionary.get_todays_pair(date.today().day)
    return render_template("dictionary/page.html", word = w)

# Songs
@app.route("/game/songs/random", methods = ["GET"])
def game_songs_random():
    w = songs.get_random_pair()
    return render_template("songs/page.html", word = w)

@app.route("/game/songs/daily", methods = ["GET"])
def game_songs_daily():
    w = songs.get_todays_pair(date.today().day)
    return render_template("songs/page.html", word = w)