import time
import hashlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/imdb'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    avatar = db.Column(db.String(500))
    active = db.Column(db.Boolean())
    token = db.Column(db.String(32))
    movie = db.relationship('Movie', backref='user',
                                lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.avatar = 'img/avatars/default.gif'
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self.active = False
        self.token = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()

    def __repr__(self):
        return '<User %r>' % self.username

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    image = db.Column(db.String(500))
    score = db.Column(db.Integer)
    like = db.Column(db.Integer)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, year, score, ruta, id_user):
        self.name = name
        self.year = year
        self.score = score
        self.image = ruta
        self.like = 0
        self.id_user = id_user

    def __repr__(self):
        return '<Movies %r>' % self.name
