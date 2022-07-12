from flask import Flask, render_template, request, send_from_directory
from qalist import QAList
from datetime import date
from requests import get
import os

app = Flask(__name__)
IP = get('https://api.ipify.org').content.decode('utf8')
IP = "http://127.0.0.1:5000"

QADictionary = {"dictionary": QAList("data/words.csv", 3, 0),
                "songs": QAList("data/songs.csv", 0, 1)
}

question_name = {"songs": "Title",
                 "dictionary": "Definition"
}

answer_name = {"songs": "Artist",
               "dictionary": "Word"
}

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route("/", methods = ["GET"])
def index():
    return "<p>Word of the day API. Access through /api/</p>"

# API
@app.route("/api/<list_to_use>/<mode>", methods = ["GET"])
def api(list_to_use: str, mode: str):
    if mode == "random":
        w = QADictionary[list_to_use].get_random_pair()
        return {"answer": w.answer, "question": w.question}
    if mode == "daily":
        w = QADictionary[list_to_use].get_todays_pair(date.today().day)
        return {"answer": w.answer, "question": w.question}

# GAME
@app.route("/game/<list_to_use>/<mode>", methods = ["GET"])
def game(list_to_use: str, mode: str):
    return render_template(f"game/page.html", IP = IP, list_to_use = list_to_use, mode = mode, question_name = question_name[list_to_use], answer_name = answer_name[list_to_use])