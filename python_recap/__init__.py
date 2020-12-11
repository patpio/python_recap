from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    python_recap = Flask(__name__)

    python_recap.config.from_object('python_recap.config.DevelopmentConfig')

    from .views import bp_main
    from .views import bp_flashcard
    from .views import bp_auth
    from .views import bp_user

    python_recap.register_blueprint(bp_main)
    python_recap.register_blueprint(bp_flashcard)
    python_recap.register_blueprint(bp_auth)
    python_recap.register_blueprint(bp_user)

    db.init_app(python_recap)
    Migrate(python_recap, db)

    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(python_recap)

    return python_recap
