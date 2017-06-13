from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class NewForm(Form):
    empresa = StringField('Empresa', validators=[InputRequired('Debe introducir un título.'), Length(1, 100, 'Su título es demasiado largo.')])
    puesto = StringField('Puesto', validators=[InputRequired('Debe introducir un título.'), Length(1, 100, 'Su título es demasiado largo.')])
    anyo_inicio = IntegerField('Año de inicio', validators=[InputRequired('No puede hacer una nota vacía')])
    anyo_salida = IntegerField('Año de salida', validators=[InputRequired('No puede hacer una nota vacía')])
    submit = SubmitField('Crear')

class EditForm(Form):
    empresa = StringField('Empresa', validators=[InputRequired('Debe introducir un título.'), Length(1, 100, 'Su título es demasiado largo.')])
    puesto = StringField('Puesto', validators=[InputRequired('Debe introducir un título.'), Length(1, 100, 'Su título es demasiado largo.')])
    anyo_inicio = IntegerField('Año de inicio', validators=[InputRequired('No puede hacer una nota vacía')])
    anyo_salida = IntegerField('Año de salida', validators=[InputRequired('No puede hacer una nota vacía')])
    submit = SubmitField('Crear')

class UserForm(Form):
    name = StringField('Usuario', validators=[InputRequired('Necesitas indicar tu nombre.'), Length(1, 100, 'Su Nombre es demasiado largo.')])
    email = StringField('Email', validators=[InputRequired('Debe introducir un correo.'), Email('Su Email es demasiado largo.')])
    password = PasswordField('Contraseña', validators=[InputRequired('Necesita introducir una contraseña')])
    password2 = PasswordField('Repite contraseña', validators=[InputRequired('Necesita introducir una contraseña')])
    submit = SubmitField('Crear')