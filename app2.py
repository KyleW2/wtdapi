from flask import Flask, render_template, request
from qalist import QAList
from datetime import date
from requests import get

app = Flask(__name__)
IP = get('https://api.ipify.org').content.decode('utf8')

songs = QAList("data/songs.csv", 0, 1)

@app.route("/", methods = ["GET"])
def index():
    return "<p>Word of the day API. Access through /api/</p>"

# API
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
# Songs
@app.route("/game/songs/random", methods = ["GET"])
def game_songs_random():
    w = songs.get_random_pair()
    return render_template("songs/page.html", IP = IP)

@app.route("/game/songs/daily", methods = ["GET"])
def game_songs_daily():
    w = songs.get_todays_pair(date.today().day)
    return render_template("songs/page.html", word = w)