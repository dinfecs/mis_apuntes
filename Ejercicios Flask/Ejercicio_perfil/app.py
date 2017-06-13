from flask import Flask, render_template, redirect, url_for, request
from Item import Item
from forms import EditForm
from time import time
from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key = 'secret'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png'])


perfil_items = Item('Marco', 'Alarcón', 'Esto es una descripción super larga porque no se que escribir.', 'img/perfil.png')

@app.route("/")
def index():
    return render_template('items/perfil.html', perfil=perfil_items)

@app.route("/modificar_perfil")
def modificar_perfil():
    form = EditForm()
    return render_template('items/perfil_edit.html', form=form)

@app.route("/perfil_modificado", methods=['POST'])
def perfil_modificado():
    form = EditForm()
    if form.validate_on_submit():
        f = request.files['imagen']
        nombre = str(int(time())) + f.filename
        nombre_con_hora = secure_filename(nombre)
        import os, sys
        base_dir = sys.path[0]
        f.save(os.path.join(base_dir, 'static/img/' + nombre_con_hora))
        perfil_items.nombre = request.form['nombre']
        perfil_items.apellido = request.form['apellido']
        perfil_items.descripcion = request.form['descripcion']
        perfil_items.imagen = 'img/' + nombre_con_hora
        return redirect(url_for('index'))
    else:
        return render_template('items/perfil_edit.html', form=form, todos_errores=form.errors.items())

if __name__ == "__main__":
    app.debug = True
    app.run()