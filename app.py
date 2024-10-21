from flask import flask

app = flask(__name__)

@app.route("/")
def index(self):
    return "<h1>olá<br>mundo</h1>"

@app.route("/aluno/<nome>")
def aluno(nome):
    return nome