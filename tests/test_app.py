"""
Set up the test client, intialize the database
"""

import pytest
from app import create_app, db

from app.models import User, Post

@pytest.fixture()
def app():
    app = create_app('test_config.TestConfig')

    with app.app_context():
        print("Check:::", app.url_map)
        #Create the database
        db.create_all()

        yield app

        db.session.close()
        db.drop_all()

@pytest.fixture()
def client(app):
    #for creating a Flask test client.
    return app.test_client()

@pytest.fixture()
def init_database(app):

    with app.app_context():
        userA = User(username='userA', email='userA@gmail.com')
        db.session.add(userA)
        db.session.commit()

        postA = Post(user_id=userA.id, content='Hello, World, this is my first post')
        db.session.add(postA)
        db.session.commit()

        yield db

        db.session.remove()
        db.drop_all()




