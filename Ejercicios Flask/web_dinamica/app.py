from flask import Flask, render_template, url_for
from Enlace import Enlace
from form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreto'

@app.route("/")
def index():
    menu = [Enlace(url_for('index'), 'Home'), Enlace(url_for('contact'), 'Contact')]
    return render_template('items/home.html', menu=menu)
@app.route("/contact")
def contact():
    form = ContactForm()
    menu = [Enlace(url_for('index'), 'Home'), Enlace(url_for('contact'), 'Contact')]
    return render_template('items/contact.html', menu=menu, form=form)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")