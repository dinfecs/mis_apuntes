from flask import Flask, render_template, redirect, url_for, request
from Item import Item
from forms import NewForm
from werkzeug import secure_filename
from time import time

app = Flask(__name__)
app.secret_key = 'secret'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png'])

list_items = [Item(1, 'Pegatina', 4, 'Es una cosa chula', 'img/pegatinas1.jpg'),
              Item(2, 'Cosica', 50, 'Es una cosa chula', 'img/pegatinas2.jpg'),
              Item(3, 'Esternocleidomastoideo', 72, 'Es una cosa chula', 'img/pegatinas3.jpg'),
              Item(4, 'Supercalifragili', 85, 'Es una cosa chula', 'img/pegatinas4.jpg')]
carrito = []

@app.route("/")
def index():
    total = 0
    #calcular el precio final
    for producto in carrito:
        for item in list_items:
            if producto == item.id:
                total += item.precio
    #imprimimos
    return render_template('items/tienda.html', items=list_items, carrito=carrito, total=total)

@app.route("/add/<int:id>")
def add(id):
    carrito.append(id)
    return redirect(url_for('index'))

@app.route("/new")
def new():
    form = NewForm()
    return render_template('items/new.html', form=form)
@app.route("/new_product", methods=['POST'])
def new_product():
    form = NewForm()
    if form.validate_on_submit():
        id_end = list_items[-1]
        id_end = int(id_end.id) + 1
        f = request.files['imagen']
        nombre = str(int(time())) + f.filename
        nombre_con_hora = secure_filename(nombre)
        import os, sys
        base_dir = sys.path[0]
        f.save(os.path.join(base_dir, 'static/img/' + nombre_con_hora))
        list_items.append(Item(id_end, request.form['nombre'], float(request.form['precio']), request.form['descripcion'], 'img/' + nombre_con_hora))
        return redirect(url_for('index'))
    else:
        return render_template('items/new.html', form=form, todos_errores=form.errors.items())

if __name__ == "__main__":
    app.debug = True
    app.run()