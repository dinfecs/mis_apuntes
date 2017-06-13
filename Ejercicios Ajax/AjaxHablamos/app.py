from flask import Flask, render_template, url_for, request, jsonify
from random import randint
from models import db, Mensajes
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('oraculo.html')

@app.route("/mensajes")
def get():
    mensajes = Mensajes.query.all()
    return jsonify([i.serialize for i in mensajes])

@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        mi_mensaje = Mensajes(request.form['apodo'], request.form['mensaje'])
        db.session.add(mi_mensaje)
        try:
            db.session.commit()
        except:
            db.session.rollback()
    return 'ok'

if __name__ == "__main__":
    app.debug = True
    app.run()