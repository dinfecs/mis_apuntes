# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/perfil/<nombre>") # Cualquier cosa
def verPerfil(nombre):
    return "<h1>Bienvenido {0}</h1>".format(nombre)

@app.route("/edad/<int:anyos>") # Solo números enteros
def verificarEdad(anyos):
    if anyos < 18:
        return "<h1>Eres menor de edad, pillin... Pasa</h1>" 
    else:
        return "<h1>Pasa hombretón</h1>" 

@app.route("/peso/<float:peso>") # Solo números con decimales 
def verificarPeso(peso):
    html = '<h1>Tu peso es de {0} Kg'.format(peso)
    if peso > 100:
        html += "<h1>Deberíamos cuidarnos con los bombones</h1>" 
    return html

@app.route("/url/<path:ruta>") # Como el default, salvo que también admite slashs
def enlace(ruta):
    return "<h1>La ruta: {0}</h1>".format(ruta)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
