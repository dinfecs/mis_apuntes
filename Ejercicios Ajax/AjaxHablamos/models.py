from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import hashlib
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/chat'
db = SQLAlchemy(app)


class Mensajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apodo = db.Column(db.String(100))
    mensaje = db.Column(db.String(500))


    def __init__(self, apodo, mensaje):
        self.apodo = apodo
        self.mensaje = mensaje

    def __repr__(self):
        return '<Mensajes %r>' % self.apodo

    @property
    def serialize(self):
        return {
            'id': self.id,
            'apodo': self.apodo,
            'mensaje': self.mensaje
        }