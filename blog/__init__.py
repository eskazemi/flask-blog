from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = '20087e54287ebc42171363753890098b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../blog.db"

db = SQLAlchemy(app)

from blog import routes