from flask import Flask, render_template, request,redirect, url_for
from Hero import Heroe
from enlace import Enlace
app = Flask(__name__)

lista_heroes = [Heroe('Batman', 'Millonario aburrido', 2), Heroe('Wonderwoman', 'un latigo con clase', 1)]

@app.route("/")
def index():
    return render_template('lista_superhero.html', heroes=lista_heroes)


@app.route("/guardar", methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    sexo = request.form['sexo']
    lista_heroes.append(Heroe(nombre, descripcion, int(sexo)))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()
