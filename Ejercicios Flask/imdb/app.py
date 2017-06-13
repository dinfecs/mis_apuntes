# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, flash, session
from forms import User_form, New_movie, Search_form, Perfil_form
from models import User, db, Movie
from flask_mail import Mail, Message
import hashlib
import math
import os
import time
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/img/portadas/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SECRET_KEY'] = 'secret'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USERNAME'] = 'asd@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

LIMITE_PELICULAS = 5

@app.route("/")
def login():
    form = User_form()
    if request.args.get('email') and request.args.get('password1'):
        email = request.args.get('email')
        password = hashlib.md5(request.args.get('password1').encode('UTF-8')).hexdigest()
        my_user = User.query.filter_by(email=email, password=password).first()
        if my_user:
            # Existe
            session['user'] = my_user.id
            return redirect(url_for('dashboard'))
        else:
            # No Existe
            flash('El usuario o contraseña no está registrado.')
    return render_template('items/login.html', form=form)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/peliculas/", methods=['GET', 'POST'], defaults={'pag': 1})
@app.route("/peliculas/<int:pag>", methods=['GET', 'POST'])
def dashboard(pag):
    form = New_movie()
    form_search = Search_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Movemos la imagen a static
            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                hora_unix = int(time.time())
                ruta = str(hora_unix) + filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], ruta))
            else:
                flash('Debe ser una imagen.')
            # Guardamos la info en la base de datos
            my_movie = Movie(request.form['name'], request.form['year'], request.form['score'], ruta, session['user'])
            db.session.add(my_movie)
            try:
                db.session.commit()
                flash('Añadido correctamente', 'success')
            except:
                db.session.rollback()
        else:
            #mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    movies = Movie.query.limit(LIMITE_PELICULAS * pag).offset(LIMITE_PELICULAS * (pag - 1)).all()
    num_movies = Movie.query.count()
    num_paginas = math.ceil(num_movies / LIMITE_PELICULAS)
    # Obtenemos el usuario
    my_user = User.query.filter_by(id=session['user']).first()
    return render_template('items/dashboard.html', form=form, movies=movies, num_paginas=num_paginas, LIMITE_PELICULAS=LIMITE_PELICULAS, form_search=form_search, user=my_user)

@app.route("/search/<ordenar>")
def search(ordenar):
    movies = False
    form = New_movie()
    form_search = Search_form()

    if ordenar == 'year':
        movies = Movie.query.order_by(Movie.year)
    elif ordenar == 'name':
        movies = Movie.query.order_by(Movie.name)

    return render_template('items/dashboard.html', movies=movies, form=form, form_search=form_search, num_paginas=0)


@app.route("/filter")
def filter():
    form = New_movie()
    form_search = Search_form()
    name = request.args.get('name')
    year = request.args.get('year')
    movies = Movie.query.filter(Movie.name.like(f'%{name}%')).filter(Movie.year.like(f'%{year}%')).all()

    return render_template('items/dashboard.html', movies=movies, form=form, form_search=form_search, num_paginas=0)



@app.route("/confirmar/<token>")
def confirmar(token):
    my_user = User.query.filter_by(token=token).first()
    if my_user:
        my_user.active = True
        db.session.add(my_user)
        try:
            flash('Su cuenta ha sido activada.', 'success')
            db.session.commit()
        except:
            db.session.rollback()
    else:
        flash('Enlace caducado', 'danger')
    return redirect(url_for('login'))



@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = User_form()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form['email']
            my_user = User.query.filter_by(email=email).first()
            if not my_user:
                if request.form['password1'] == request.form['password2']:
                    my_user = User(request.form['username'], request.form['email'], request.form['password1'])
                    db.session.add(my_user)
                    try:
                        db.session.commit
                        db.session.commit()
                        # Envio de email
                        msg = Message("Hello",
                            sender="no-reply@idecrea.es",
                            recipients=[my_user.email])
                        link_token = f'http://localhost:5000/confirmar/{my_user.token}'
                        msg.html = render_template(
                                'email/confirmar.html',
                                link_token=link_token)
                        mail.send(msg)
                        # Informamos al usuario
                        flash('Le acabamos de enviar un email con las instrucciones. Gracias.', 'success')

                    except:
                        db.session.rollback()
                        flash('Disculpe, ha ocurrido un error.', 'danger')
                    return redirect(url_for('login'))
                else:
                    flash('Los passwords no son iguales', 'danger')
            else:
                flash('El e-mail ya esta registrado', 'danger')
        else:
            # Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/signup.html', form=form)

@app.route("/close")
def close_session():
    session.clear()
    return redirect(url_for('dashboard'))


@app.route("/like/<movie>")
def add_like(movie):
    movie_like = Movie.query.filter_by(id=movie).first()
    movie_like.like = movie_like.like + 1
    db.session.add(movie_like)
    db.session.commit()
    return ''


@app.route("/perfil", methods=['GET', 'POST'])
def perfil():
    form = Perfil_form()
    my_user = User.query.filter_by(id=session['user']).first()
    if request.method == 'POST':
        # Comprobamos si desean cambiar la contraseña
        if request.form['password_anterior'] and request.form['password_nueva']:
            # Comprobamos que la contraseña anterior es igual a la que ya estaba
            if hashlib.md5(request.form['password_anterior'].encode('utf-8')).hexdigest() == my_user.password:
                # Modificamos
                my_user.password = hashlib.md5(request.form['password_nueva'].encode('utf-8')).hexdigest()
                db.session.add(my_user)
                try:
                    db.session.commit()
                    flash('Su contraseña ha sido modificada correctamente', 'success')
                except:
                    db.session.rollback()
            else:
                flash('Su contraseña anterior no es igual. ¿Eres tú?', 'danger')
        # Cambiar el username
        my_user.username = request.form['username']
        db.session.add(my_user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
        # Cambiamos el avatar
        file = request.files['avatar']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            hora_unix = int(time.time())
            ruta = str(hora_unix) + filename
            file.save(os.path.join('static/img/avatars/', ruta))
            # Borramos la imagen anterior
            if my_user.avatar != 'img/avatars/default.gif':
                os.remove(os.path.join('static', my_user.avatar))
            # Guardamos la ruta en la base de datos
            my_user.avatar = os.path.join('img/avatars/', ruta)
            db.session.add(my_user)
            try:
                db.session.commit()
            except:
                db.session.rollback()
        else:
            flash('Debe ser una imagen.', 'danger')
        # Redireccionamos
        flash('Actualizado correctamente', 'success')
        return redirect(url_for('dashboard'))


    return render_template('items/perfil.html', form=form, user=my_user)

if __name__ == "__main__":
    app.debug = True
    app.run()