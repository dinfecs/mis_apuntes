from flask import Flask, render_template, redirect, url_for, request
from Item import Item

app = Flask(__name__)
app.secret_key = 'secret'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png'])

post_blog = [Item('Este lunes Marc se perderá la clase de SQL',
                  'El pasado viernes el alumno Marc, de la escuela Idecrea, ha decidido irse de fiesta a Madrid y volver el día lunes, perdiendo la clase final de SQL donde Andros enseñara a concadenar las bases de datos con nuesta pagina web',
                  'img/post1.jpg'),
             Item('He comprado leche XD',
                  'Ayer fui al mercadona a comprar leche y volvi a casa como si nada porque yo lo valgo.',
                  'img/post2.jpg'),
             Item('¿Baila tu cuerpo alegría macarena?',
                  'Que tu cuerpo fragante alegría cosa buena, baila tu cuerpo alegría macarena EHHHHHHHHHHHHH macarena aaaaAAAAHH',
                  'img/post3.jpg')]

@app.route("/")
def index():
    return render_template('items/blog.html', blog=post_blog)

if __name__ == "__main__":
    app.debug = True
    app.run()