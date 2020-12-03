import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    python_recap = Flask(__name__)

    python_recap.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'python_recap.db')}"
    python_recap.config['SECRET_KEY'] = 'pint'

    from python_recap.views import bp_main
    python_recap.register_blueprint(bp_main)

    db.init_app(python_recap)
    Migrate(python_recap, db)

    return python_recap
