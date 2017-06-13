from flask import Flask, render_template, redirect, url_for, request, flash
from forms import NewForm, EditForm
from DB import Note, db

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def index():
    notas = Note.query.all()
    return render_template('items/dashboard.html', notas=notas)

@app.route("/new", methods=['GET', 'POST'])
def new_note():
    form = NewForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Guardamos en la base de datos
            flash('Guardado bien', 'success')
            my_note = Note(request.form['title'], request.form['text'])
            db.session.add(my_note)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            return redirect(url_for('index'))
        else:
            # Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/new.html', form=form)

@app.route("/note/<int:id>")
def view_note(id):
    my_note = Note.query.filter_by(id=id).first()
    return render_template('items/note.html', note=my_note)

@app.route("/delete/<int:id>")
def delete_note(id):
    my_note = Note.query.filter_by(id=id).first()
    db.session.delete(my_note)
    try:
        db.session.commit()
        flash('Eliminado', 'success')
    except:
        db.session.rollback()
        flash('ME CAGO EN TODO HA OCURRIDO UN ERROR', 'danger')
    return redirect(url_for('index'))

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_note(id):
    my_note = Note.query.filter_by(id=id).first()
    form = EditForm(title=my_note.title, text=my_note.text)
    if request.method == 'POST':
        if form.validate_on_submit():
            # Guardamos en la base de datos
            flash('Guardado bien', 'success')
            my_note.title = request.form['title']
            my_note.text = request.form['text']
            db.session.add(my_note)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            return redirect(url_for('index'))
        else:
            # Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/edit.html', form=form, note=my_note)

if __name__ == "__main__":
    app.debug = True
    app.run()