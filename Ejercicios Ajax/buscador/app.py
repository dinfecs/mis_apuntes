# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from models import db, Paises
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('buscador.html')


@app.route("/busqueda/<q>")
def buscar(q):
    paises = Paises.query.filter(Paises.nombre.like('%' + q + '%')).all()
    return jsonify([i.serialize for i in paises])


if __name__ == "__main__":
    app.debug = True
    app.run()
