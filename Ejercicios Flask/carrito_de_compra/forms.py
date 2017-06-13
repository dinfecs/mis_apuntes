from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, FileField
from wtforms.validators import Required, Length, NumberRange, InputRequired

class NewForm(Form):
    nombre = StringField('Nombre', validators=[InputRequired('Obligatorio')])
    precio = IntegerField('Precio', validators=[InputRequired('Obligatorio'), NumberRange(0.01, 10000, 'El precio es obligatorio')])
    descripcion = TextAreaField('Descripción', validators=[InputRequired('Necesitamos una descripción')])
    imagen = FileField('Imagen', validators=[InputRequired('Necesitamos una imagen')])
    submit = SubmitField('Salvar')