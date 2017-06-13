# -*- coding: utf-8 -*-
from flask import Flask, render_template
from Mensaje import Mensaje

# Variables
app = Flask(__name__)
list_mensajes = [Mensaje('Juan', 'Yo te bautizo'), Mensaje('Torrente', 'Viva el Betis')]

@app.route("/", )
def index():
    return render_template('index.html', mensajes=list_mensajes)

if __name__ == "__main__":
    app.debug = True
    app.host = '0.0.0.0'
    app.run()