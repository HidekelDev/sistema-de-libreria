from app import create_app, db
from app.models.book import Book


def test_catalog_route():
    class TestConfig:
        TESTING = True
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    app = create_app(config_class=TestConfig)
    with app.app_context():
        db.create_all()
        b = Book(title='Libro API', author='Autor', isbn='api-1', total_copies=1, available_copies=1)
        db.session.add(b)
        db.session.commit()
        client = app.test_client()
        rv = client.get('/catalogo')
        assert rv.status_code == 200
        assert b'titulo' not in rv.data.lower()  # just ensure page rendered
