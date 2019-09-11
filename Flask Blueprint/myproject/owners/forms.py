# owners/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):

    name = StringField('Owner Name: ')
    kit_id = IntegerField('Kittend ID: ')
    submit = SubmitField('Add Owner')
