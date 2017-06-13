from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, TextAreaField

class ContactForm(Form):
    name = StringField('Nombre')
    email = StringField('Email')
    phone = IntegerField('Telefono')
    menssage = TextAreaField('Mensaje')
    submit = SubmitField('Registrarse')