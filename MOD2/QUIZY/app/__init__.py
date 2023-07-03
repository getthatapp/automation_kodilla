from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .auth import bp as auth_bp

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .models import user, quiz
    from .forms import RegistrationForm, LoginForm

    return app