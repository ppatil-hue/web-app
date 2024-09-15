"""
Initialize Flask App
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class=None):

    app = Flask(__name__)

    if config_class:  # to be used for production and testing environments
        app.config.from_object(config_class)
    else:
        app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes import register_routes
    register_routes(app)

    return app
