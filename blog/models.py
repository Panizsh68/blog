from blog import db
import datetime

class User(db.Model):
    __table_args__ = {"extend_existing": True} 
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False) 
    email = db.Column(db.String(60), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref=db.backref('posts_author', lazy= True), lazy= True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.username}, {self.email})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.datetime.now)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f'{self .__class__.__name__}({self.id}, {self.title}, {self.date})'

# >>> p1 = Post(title= 'nature', content= 'holiday in nature with family')
# >>> p1 = Post(posts_author = u1)
# >>> u1 = User(username= 'paniz', email= 'panizshaabanpour16@gmail.com', password= '123')