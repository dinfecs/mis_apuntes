from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import InputRequired

class EditForm(Form):
    titulo = StringField('Nombre', validators=[InputRequired('Obligatorio')])
    post = TextAreaField('Post', validators=[InputRequired('No puedes publicar un Post en blanco')])
    imagen = FileField('Imagen', validators=[InputRequired('Se necesita una imagen')])
    submit = SubmitField('Salvar')