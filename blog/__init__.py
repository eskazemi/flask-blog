from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SECRET_KEY"] = '20087e54287ebc42171363753890098b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../blog.db"

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

from blog import routes