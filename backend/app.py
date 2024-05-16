from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from db.characters import get_all_characters

@app.route("/")
def home():
    return "Home Page"

@app.route("/characters")
def all_characters():
    return get_all_characters()