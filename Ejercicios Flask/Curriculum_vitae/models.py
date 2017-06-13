from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/curriculum_vitae'
db = SQLAlchemy(app)


class Experiencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(80))
    puesto = db.Column(db.String(100))
    anyo_inicio = db.Column(db.Integer)
    anyo_salida = db.Column(db.Integer)

    def __init__(self, empresa, puesto, anyo_inicio, anyo_salida):
        self.empresa = empresa
        self.puesto = puesto
        self.anyo_inicio = anyo_inicio
        self.anyo_salida = anyo_salida

    def __repr__(self):
        return '<Experiencia {0}>'.format(self.puesto)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()

    def __repr__(self):
        return '<User {0}>'.format(self.email)