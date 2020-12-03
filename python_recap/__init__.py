from flask import Flask


def create_app():
    python_recap = Flask(__name__)

    from python_recap.views import bp_main

    python_recap.register_blueprint(bp_main)

    return python_recap
