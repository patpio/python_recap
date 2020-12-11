from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

from ..models.user_model import User

bp_user = Blueprint('users', __name__, url_prefix='/users')


@bp_user.route('/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()

    if current_user == user:
        return render_template('user.html', user=user)

    abort(404)
