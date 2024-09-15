from flask import Flask, request
from flask import jsonify
from .models import User, Post
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

def register_routes(app):

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({'message': 'Hello, World!'}), 200

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201


    @app.route('/posts', methods=['POST'])
    def create_post():
        data = request.get_json()
        user = User.query.filter_by(id=data['user_id']).first()
        if user:
            post = Post(user_id=user.id, content=data['content'])
            db.session.add(post)
            db.session.commit()
            return jsonify({'message': 'Post created successfully'}), 201
        else:
            return jsonify({'message': 'User not found'}), 404

    @app.route('/posts', methods=['GET'])
    def get_posts_for_user():
        user_id = request.args.get('user_id')
        user = User.query.filter_by(id=user_id).first()
        if user:
            posts = Post.query.filter_by(user_id=user.id).all()
            return jsonify([post.serialize() for post in posts]), 200
        else:
            return jsonify({'message': 'User not found'}), 404

    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify(
           [{
            'id': user.id,
            'username': user.username,
            'email': user.email
            } for user in users ]), 200







