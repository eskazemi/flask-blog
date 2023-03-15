from blog import app
from flask import render_template
from blog.forms import RegistrationForm


@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", form=form)


@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template("login.html", form=form)
