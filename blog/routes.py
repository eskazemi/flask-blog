from blog import app
from flask import render_template


@app.route("/")
def get_name():
    return render_template('home.html')