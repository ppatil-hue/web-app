from app import db
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

    # Backref for posts and newsfeed items
    posts = db.relationship('Post', backref='author', lazy=True)
    newsfeed_items = db.relationship('Newsfeed', backref='user', lazy=True)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())

    # Backref to newsfeed
    feed_items = db.relationship('Newsfeed', backref='post', lazy=True)


class Newsfeed(db.Model):
    __tablename__ = 'newsfeeds'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    relevance_score = db.Column(db.Float, nullable=True)
