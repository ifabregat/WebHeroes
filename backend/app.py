from flask import Flask
from flask_cors import CORS
from time import sleep

app = Flask(__name__)
CORS(app)

from db.characters import get_all_characters, get_character_by_id, remove_character

@app.route("/")
def home():
    return ""

@app.route("/characters")
def all_characters():
    return get_all_characters()

@app.route("/characters/<id>")
def character_by_id(id):
    sleep(1)
    return get_character_by_id(id)

@app.route("/characters/<id>", methods = ["DELETE"])
def remove_character_by_id(id):
    return {"success": remove_character(id)}