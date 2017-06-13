from flask import Flask, redirect, url_for, render_template, request, flash, session

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('layouts/main.html')

if __name__ == "__main__":
    app.debug = True
    app.run()

