# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Estas en el inicio</h1><a href='/Info'>Info</a>" 

@app.route("/Info")
def info():
    return "<h1>Información para todos</h1>" 


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
