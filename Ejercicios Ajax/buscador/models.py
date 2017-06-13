from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/mundo'
db = SQLAlchemy(app)

class Paises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))

    def __repr__(self):
        return '<Paises %r>' % self.nombre

    @property
    def serialize(self):
        return {
            'nombre': self.nombre
        }