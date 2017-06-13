from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/correos'
db = SQLAlchemy(app)

class Correos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100))

    def __repr__(self):
        return '<Correos %r>' % self.correo

    @property
    def serialize(self):
        return {
            'correo': self.correo
        }