from flask import Blueprint, render_template


from ..models.user_model import User
from python_recap import login_manager

bp_main = Blueprint('main', __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp_main.route('/')
def home():
    return render_template('index.html')


@bp_main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@bp_main.app_errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@bp_main.app_errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
