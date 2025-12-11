import pytest
from app import create_app, db
from app.models.user import User


@pytest.fixture
def app():
    class TestConfig:
        TESTING = True
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = 'test-secret'

    app = create_app(config_class=TestConfig)
    with app.app_context():
        db.create_all()
        yield app


def test_register_and_login(app):
    client = app.test_client()
    # register
    rv = client.post('/register', data={'username': 'test', 'email': 'a@b.com', 'password': 'pass'}, follow_redirects=True)
    assert b'Registro exitoso' in rv.data or rv.status_code == 200
    # check user in DB
    with app.app_context():
        u = User.query.filter_by(username='test').first()
        assert u is not None
    # login
    rv2 = client.post('/login', data={'username': 'test', 'password': 'pass'}, follow_redirects=True)
    assert rv2.status_code == 200
