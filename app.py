from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import *
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

today = date.today()
formatted_date = today.strftime(" %m/%d/%y ")


@app.route('/')
def show_home():
    """Show Home Page"""
    return render_template("home.html", date=formatted_date)


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome",
               "Pythonic", "nice", "intelligent", "wise", "fun"]


@app.route('/form')
def show_form():
    """Show version 2 greeting form, adding checkbox for compliments"""
    return render_template("form.html")


@app.route('/greet')
def get_greeting():
    """Return second greeting"""
    username = request.args["username"]
    wants_compliments = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    # compliment = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, wants_compliments=wants_compliments, nice_things=nice_things, date=formatted_date)


@app.route('/hello')
def hello():
    """"Return Hello Page"""
    return render_template("hello.html")


@app.route("/lucky")
def show_lucky_num():
    """"Example of simple dynamic template"""
    num = randint(1, 10)
    return render_template("lucky.html", date=formatted_date, lucky_num=num, msg=" You are so lucky!")


@app.route('/python-tips')
def python_tips():
    return render_template('python_tips.html')


@app.route('/flask-tips')
def flask_tips():
    return render_template('flask_tips.html')
