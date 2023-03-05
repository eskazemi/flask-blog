from blog import db
from datetime import datetime


class Post(db.Model):
    id = db.Colmun(db.Integer, primery_key=True)
    title = db.Colmun(db.String(30), nullable=False)
    created_at = db.Colmun(db.DateTime, nullable=False, default=datetime.now)
    content = db.Colmun(db.Text, nullable=False)
    user_id = db.Colmun(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.__clas__.__name__}-{self.id}-{self.title[:30]}"
