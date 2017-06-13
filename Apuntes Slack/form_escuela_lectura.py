from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required, Email, NumberRange

class RegistroForm(Form):
    name = StringField('Nombre', validators=[Required()])
    age = IntegerField('Edad', validators=[NumberRange(1, 100)])
    email = StringField('Email', validators=[Required(), Email()])
    submit = SubmitField('Registrarse')
