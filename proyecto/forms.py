from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Debe introducir su nombre'), Length(1, 80, 'Su nombre es demasiado largo.')])
    email = StringField('E-mail', validators=[DataRequired('Debe introducir su correo electrónico'), Email('El formato de su correo electrónico no es válido.'), Length(1, 80, 'Su email es demasiado largo.')])
    subject =  StringField('Asunto', validators=[DataRequired('Debe introducir un asunto'), Length(1, 80, 'Su asunto es demasiado largo.')])
    message = TextAreaField("Mensaje")
    submit = SubmitField("Enviar")