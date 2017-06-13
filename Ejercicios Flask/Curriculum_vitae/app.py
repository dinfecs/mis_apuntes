from flask import Flask, render_template, url_for, flash, redirect, request, session
from models import db, Experiencia, User
from flask_sqlalchemy import SQLAlchemy
from forms import NewForm, EditForm, UserForm
from functools import wraps
import hashlib
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

def login_required(f):
    # Decoration: check login in session
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            session.clear()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/dashboard")
@login_required
def index():
    my_experiencia = Experiencia.query.order_by(Experiencia.anyo_salida.desc())
    return render_template('items/curriculum_vitae.html', experiencia=my_experiencia)

@app.route("/experiencia/<int:id>")
@login_required
def borrar_experiencia(id):
    my_experiencia = Experiencia.query.filter_by(id=id).first()
    db.session.delete(my_experiencia)
    try:
        db.session.commit()
        flash('EXPERIENCIA ELIMINADA', 'success')
    except:
        db.session.rollback()
        flash('HA OCURRIDO UN ERROR', 'danger')
    return redirect(url_for('index'))

@app.route("/new", methods=['GET', 'POST'])
@login_required
def new_experience():
    form = NewForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Guardamos en la base de datos
            flash('Guardado bien', 'success')
            my_experience = Experiencia(request.form['empresa'], request.form['puesto'], request.form['anyo_inicio'], request.form['anyo_salida'])
            db.session.add(my_experience)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            return redirect(url_for('index'))
        else:
            # Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/new.html', form=form)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_experience(id):
    my_experience = Experiencia.query.filter_by(id=id).first()
    form = EditForm(empresa=my_experience.empresa, puesto=my_experience.puesto, anyo_inicio=my_experience.anyo_inicio, anyo_salida=my_experience.anyo_salida)
    if request.method == 'POST':
        if form.validate_on_submit():
            # Guardamos en la base de datos
            flash('Guardado bien', 'success')
            my_experience.empresa = request.form['empresa']
            my_experience.puesto = request.form['puesto']
            my_experience.anyo_inicio = request.form['anyo_inicio']
            my_experience.anyo_salida = request.form['anyo_salida']
            db.session.add(my_experience)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            return redirect(url_for('index'))
        else:
            # Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/edit.html', form=form, note=my_experience)

@app.route("/", methods=['GET', 'POST'])
def login():
    form = UserForm()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password = hashlib.md5(password.encode('UTF-8')).hexdigest()
        my_user = User.query.filter_by(email=email, password=password).first()
        if my_user:
            session['email'] = email
            return redirect(url_for('index'))
        else:
            flash('Su email o contraseña es incorrecta.', 'danger')
    return render_template('items/login.html', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Guardamos en la base de datos
            if request.form['password'] == request.form['password2']:
                flash('Creado usuario correctamente', 'success')
                my_user = User(request.form['name'], request.form['email'], request.form['password'])
                db.session.add(my_user)
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
                return redirect(url_for('login'))
            else:
                flash('las contraseñas no son iguales.')
        else:
            # Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/signup.html', form=form)

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.debug = True
    app.run()