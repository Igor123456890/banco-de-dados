from flask import flask

app = flask(__name__)

@app.route("/")
def index(self):
    return "olá mundo"