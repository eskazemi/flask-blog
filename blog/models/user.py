from blog import db


class User(db.Model):
    id = db.Colmun(db.Integer, primery_key=True)
    username = db.Colmun(db.String(30), unique=True, nullable=False)
    email = db.Colmun(db.String(30), unique=True, nullable=False)
    password = db.Colmun(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="auther", lazy=True)


    def __repr__(self):
        return f"{self.__clas__.__name__}-{self.id}-{self.username}"

