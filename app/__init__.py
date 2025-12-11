from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        # import blueprints
        from .routes.auth import auth_bp
        from .routes.books import books_bp
        from .routes.loans import loans_bp
        from .routes.admin import admin_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(books_bp)
        app.register_blueprint(loans_bp)
        app.register_blueprint(admin_bp)

        # create DB tables if they don't exist
        try:
            db.create_all()
        except Exception:
            pass

    return app
