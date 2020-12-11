from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField


class FlashCardForm(FlaskForm):
    type = SelectField('Type', choices=[('1', 'Basic'), ('2', 'Advanced')])
    deck = StringField('Deck')
    front = TextAreaField('Front')
    back = TextAreaField('Back')
    submit = SubmitField('Add')
