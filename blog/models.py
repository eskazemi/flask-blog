from blog import (
    db,
    login_manager,
)
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id: int):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="auther", lazy=True)

    def __repr__(self):
        return f"{self.__class__.__name__}-{self.id}-{self.username}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}-{self.id}-{self.title[:30]}"
