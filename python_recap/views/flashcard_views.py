from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from ..forms import FlashCardForm

bp_flashcard = Blueprint('flashcard', __name__, url_prefix='/flashcard')


@bp_flashcard.route('/add', methods=['GET', 'POST'])
def add():
    form = FlashCardForm()
    if form.validate_on_submit():
        print('sent')
        return redirect(url_for('main.home'))

    return render_template('add.html', form=form)
