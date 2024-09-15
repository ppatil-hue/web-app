"""
Initialize Flask App
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app(config_class=None):

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    if config_class:  # to be used for production and testing environments
        app.config.from_object(config_class)
    else:
        app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes import register_routes
    register_routes(app)

    return app
