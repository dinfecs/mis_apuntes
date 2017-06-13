from flask import Flask, render_template, request
from flask_mail import Mail, Message
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('.env')

app.config['SECRET_KEY']= config['DEFAULT']['SECRET_KEY']
app.config['MAIL_SERVER'] = config['DEFAULT']['EMAIL_HOST']
app.config['MAIL_USERNAME'] = config['DEFAULT']['EMAIL_USER']
app.config['MAIL_PASSWORD'] = config['DEFAULT']['EMAIL_PASSWORD']
app.config['MAIL_PORT'] = config['DEFAULT']['EMAIL_PORT']
app.config['MAIL_USE_SSL'] = config['DEFAULT']['EMAIL_SSL']

mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def contacto():
    if request.method == 'post':
        msg = Message("Hello",
                      sender="dinfecs@gmail.com",
                      recipients=["dinfecs@gmail.com"])
        msg.body = "testing"
        msg.html = "<b>Testing</b>"
        mail.send(msg)
    return render_template('formularioEmail.html')

if __name__ == "__main__":
    app.debug = True
    app.run()