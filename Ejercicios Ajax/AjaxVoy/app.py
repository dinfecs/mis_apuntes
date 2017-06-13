from flask import Flask, render_template, url_for
from random import randint
app = Flask(__name__)

bola = ('Yo que tu no saldría a la calle', 'No lo dudes', 'Cuidado con el perro', 'No te puedo solucionar la vida', 'A mi que me cuentas solo soy una bola 8')

@app.route("/")
def index():
    return render_template('oraculo.html')

@app.route("/info")
def info():
    return bola[randint(0, len(bola) - 1)]

if __name__ == "__main__":
    app.debug = True
    app.run()