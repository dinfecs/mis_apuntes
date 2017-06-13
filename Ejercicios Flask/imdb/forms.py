from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from datetime import datetime


class User_form(FlaskForm):
    username = StringField('Nombre', validators=[
        DataRequired('Debe introducir su nombre'), 
        Length(1, 100, 'Su nombre no debe superar los 100 carácteres')
        ])
    email = StringField('E-mail', validators=[
        DataRequired('Debe introducir su correo electrónico'), 
        Email('El formato de su correo electrónico no es válido.'), 
        Length(1, 80, 'Su e-mail es demasiado largo.')])
    password1 = PasswordField('Password', validators=[DataRequired('Debe introducir su contraseña')])
    password2 = PasswordField('Repita su contraseña', validators=[DataRequired('Debe introducir su contraseña de nuevo')])
    submit = SubmitField('Registrarme')


class Perfil_form(FlaskForm):
    username = StringField('Nombre', validators=[
        DataRequired('Debe introducir su nombre'), 
        Length(1, 100, 'Su nombre no debe superar los 100 carácteres')
        ])
    password_anterior = PasswordField('Tu password actual', validators=[DataRequired('Debe introducir una contraseña')])
    password_nueva = PasswordField('Tu nuevo password', validators=[DataRequired('Debe introducir una contraseña')])
    avatar = FileField('Avatar')
    submit = SubmitField('Salvar')


class New_movie(FlaskForm):
    name = StringField('Nombre de pelicula', validators=[
        DataRequired('Debe introducir el nombre de la pelicula'),
        Length(1, 100, 'La pelicula no debe superar los 100 carácteres')])
    year = IntegerField('Fecha de estreno', validators=[
        DataRequired('Debe introducir la fecha de estreno de la pelicula'),
        NumberRange(
            1850, datetime.now().year, 'El año debe ser entre 1850 y el actual')])
    score = IntegerField('Nota', validators=[DataRequired('Debe añadir la nota de la pelicula')])
    image = FileField('Portada')
    submit = SubmitField('Añadir pelicula')


class Search_form(FlaskForm):
    name = StringField('Nombre de pelicula', validators=[Length(
        1,
        100,
        'La pelicula no debe superar los 100 carácteres')])
    year = StringField('Año de la película', validators=[
        NumberRange(
            1850,
            datetime.now().year, 'El año debe ser entre 1850 y el actual')])
    submit = SubmitField('Buscar')