# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Hola internauta!</h1>" 

if __name__ == "__main__":
    app.debug = True # Muestras mensajes que nos ayudarán en el desarrollo
    app.run(host="0.0.0.0") # Lo hace visible para el exterior
    #app.run(host="0.0.0.0", debug=True) # Otra forma
    # Pin code es para el debuger del WSGI o como medida de protección en producción
    # El servidor autorefrescará el código Python cuando cambie, pero no el navegado
