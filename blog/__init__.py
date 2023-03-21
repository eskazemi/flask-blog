from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = '20087e54287ebc42171363753890098b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../blog.db"

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please Login First"
login_manager.login_message_category = "info"

db = SQLAlchemy(app)

from blog import routes