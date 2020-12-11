from flask import Blueprint, render_template

from ..models.user_model import User

bp_user = Blueprint('users', __name__, url_prefix='/users')


@bp_user.route('/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)
