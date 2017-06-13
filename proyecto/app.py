import functools
import urllib.parse
from flask import Flask, flash, redirect, render_template, request, Response, session, url_for
from micawber import bootstrap_basic
from micawber.cache import Cache as OEmbedCache
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *
from models import Entry, FTSEntry
from forms import ContactForm
from flask_mail import Mail, Message

ADMIN_PASSWORD = 'secreto'
APP_DIR = os.path.dirname(os.path.realpath(__file__))

DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'blog.db')
DEBUG = False

SECRET_KEY = 'shhh, secreto!'

SITE_WIDTH = 800

mail = Mail()

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'testear123321@gmail.com'
app.config["MAIL_PASSWORD"] = 'a321654987'

mail.init_app(app)
app.config.from_object(__name__)

app.secret_key = 'shhh, secreto!'

flask_db = FlaskDB(app)

database = flask_db.database

oembed_providers = bootstrap_basic(OEmbedCache())

def login_required(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        if session.get('logged_in'):
            return fn(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return inner

@app.route('/login/', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next') or request.form.get('next')
    if request.method == 'POST' and request.form.get('password'):
        password = request.form.get('password')
        if password == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            session.permanent = True
            flash('Has iniciado sesión', 'success')
            return redirect(next_url or url_for('index'))
        else:
            flash('Contraseña incorrecta', 'danger')
    return render_template('items/login.html', next_url=next_url)

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        return redirect(url_for('login'))
    return render_template('items/logout.html')

@app.route('/')
def index():
    search_query = request.args.get('q')
    if search_query:
        query = Entry.search(search_query)
    else:
        query = Entry.public().order_by(Entry.timestamp.desc())
    return object_list(
        'items/index.html',
        query,
        search=search_query,
        check_bounds=False)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('Todos los campos son requeridos')
            return render_template('items/contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='testear123321@gmail.com', recipients=['testear123321@gmail.com'])
            msg.body = """
                  From: %s <%s>
                  %s
                  """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('items/contact.html',form=form, success=True)

    elif request.method == 'GET':
        return render_template('items/contact.html', form=form)

def _create_or_edit(entry, template):
    if request.method == 'POST':
        entry.title = request.form.get('title') or ''
        entry.content = request.form.get('content') or ''
        entry.published = request.form.get('published') or False
        if not (entry.title and entry.content):
            flash('Necesitas un título y un contenido para crear una entrada', 'danger')
        else:
            try:
                with database.atomic():
                    entry.save()
            except IntegrityError:
                flash('Error: Este título ya esta en uso.', 'danger')
            else:
                flash('Entrada guardada con éxito', 'success')
                if entry.published:
                    return redirect(url_for('detail', slug=entry.slug))
                else:
                    return redirect(url_for('edit', slug=entry.slug))

    return render_template(template, entry=entry)

@app.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    return _create_or_edit(Entry(title='', content=''), 'items/create.html')

@app.route('/drafts/')
@login_required
def drafts():
    query = Entry.drafts().order_by(Entry.timestamp.desc())
    return object_list('items/index.html', query, check_bounds=False)

@app.route('/<slug>/')
def detail(slug):
    if session.get('logged_in'):
        query = Entry.select()
    else:
        query = Entry.public()
    entry = get_object_or_404(query, Entry.slug == slug)
    return render_template('items/detail.html', entry=entry)

@app.route('/<slug>/edit/', methods=['GET', 'POST'])
@login_required
def edit(slug):
    entry = get_object_or_404(Entry, Entry.slug == slug)
    return _create_or_edit(entry, 'items/edit.html')

@app.template_filter('clean_querystring')
def clean_querystring(request_args, *keys_to_remove, **new_values):
    querystring = dict((key, value) for key, value in request_args.items())
    for key in keys_to_remove:
        querystring.pop(key, None)
    querystring.update(new_values)
    return urllib.parse.urlencode(querystring)

@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>¡Hala! ya lo haz roto... vuelve atras anda</h3>'), 404

def main():
    database.create_tables([Entry, FTSEntry], safe=True)
    app.run(debug=True)

if __name__ == '__main__':
    main()
