from test_app import app, client, init_database
import pytest
from app.models import User, Post
from app import db


def test_create_user(init_database):
    user = User(username='testuser', email='testuser@gmail.com')
    db.session.add(user)
    db.session.commit()

    saved_user = User.query.filter_by(username='testuser').first()
    assert saved_user.username == 'testuser'
    assert saved_user.email == 'testuser@gmail.com'

def test_get_users(client, init_database):
    response = client.get('/users')
    assert response.status_code == 200
    users = response.get_json()
    assert len(users) == 1



