# -*- coding: utf-8 -*-
from flask import Flask # Importa Flask
app = Flask(__name__) # Carga Flask

@app.route('/') # Indica la ruta que tendrá nuestra web
def inicio(): # Nombre aleatorio que le darás a la función que se ejecutará cuando se entre a esa ruta
    return '<h1>Hola mundo</h1>' # HTML que se enviará al navegador web

if __name__ == '__main__': # Verifica que se carga Flask desde Python y no desde un módulo
    app.run() # Ejecuta Flask
