def test_db_schema_exists():

    from app import create_app, db
    from app.models.book import Book

    class TestConfig:
        TESTING = True
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    app = create_app(config_class=TestConfig)
    with app.app_context():
        db.create_all()
        b = Book(title='Prueba', author='Autor', isbn='1234', total_copies=2, available_copies=2)
        db.session.add(b)
        db.session.commit()
        assert Book.query.count() == 1
