# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from models import db, Correos
import json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('buscador_correos.html')


@app.route("/busqueda/<q>")
def buscar(q):
    correos = Correos.query.filter(Correos.nombre.like('%' + q + '%')).all()
    return jsonify([i.serialize for i in correos])


if __name__ == "__main__":
    app.debug = True
    app.run()
