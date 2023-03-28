from datetime import datetime
from app import db

# if you modify this file, be sure to generate new migration:
## > flask db migrate -m <yourmessagehere>

# create User table schema for migration
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    
    # the 'Post' arg represents the "many" side of the relation.
    # the 'backref' arg will create post.author expression
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)

# create Post table schema for migration    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)