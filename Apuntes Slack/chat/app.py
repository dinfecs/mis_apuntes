# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from Mensaje import Mensaje

# Variables
app = Flask(__name__)
list_mensajes = [Mensaje('Juan', 'Yo te bautizo'), Mensaje('Torrente', 'Viva el Betis')]

@app.route("/", methods=['GET', 'POST'])
def index():
    alias = ''
    if request.method == 'POST':
        alias_form = request.form['alias']
        alias = alias_form
        text_form = request.form['mensaje']
        list_mensajes.append(Mensaje(alias_form, text_form))
    return render_template('index.html', mensajes=list_mensajes, alias=alias)

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0')