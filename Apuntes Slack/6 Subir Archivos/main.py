# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import  secure_filename
from time import time

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png'])

@app.route("/")
def index():
    return render_template('inicio.html')

@app.route('/upload', methods=['GET', 'POST'])
def subirArchivo():
    if request.method == 'POST':
        f = request.files['archivo']
        f.save('uploads/foto.jpg')
        # Parche para pycharm
        #import os, sys
        #base_dir = sys.path[0]
        #foto.save(os.path.join(base_dir,'static/galeria/foto.jpg'))

    return 'Subido'

@app.route('/uploadBien', methods=['GET', 'POST'])
def subirArchivoBien():
    if request.method == 'POST':
        f = request.files['archivo']
        f.save('uploads/' + secure_filename(f.filename))
        file.save(os.path.join(app.root_path, 'uploads', f.filename))

    return 'Subido'

@app.route('/uploadSinSobrescribir', methods=['GET', 'POST'])
def subirArchivoSinSobrescribir():
    if request.method == 'POST':
        try:
            f = request.files['archivo']
            nombre = str(int(time())) + f.filename
            f.save('uploads/' + secure_filename(nombre))
            return 'Subido'
        except:
            return 'Muy grande', 413
            
if __name__ == "__main__":
    app.run(debug=True)
