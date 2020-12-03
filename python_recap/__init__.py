import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    python_recap = Flask(__name__)

    python_recap.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'python_recap.db')}"
    python_recap.config['SECRET_KEY'] = b'&f\x91vI\xe7\xb3\x93\xafk\xe7,\xebU`\x93'

    from .views import bp_main
    from .views import bp_flashcard

    python_recap.register_blueprint(bp_main)
    python_recap.register_blueprint(bp_flashcard)

    db.init_app(python_recap)
    Migrate(python_recap, db)

    return python_recap
