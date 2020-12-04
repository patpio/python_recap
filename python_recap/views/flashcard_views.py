from flask import Blueprint, render_template, url_for
from flask_login import login_required
from werkzeug.utils import redirect

from ..forms.flashcard_forms import FlashCardForm

bp_flashcard = Blueprint('flashcard', __name__, url_prefix='/flashcard')


@bp_flashcard.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = FlashCardForm()
    if form.validate_on_submit():
        print('sent')
        return redirect(url_for('main.home'))

    return render_template('add.html', form=form)
