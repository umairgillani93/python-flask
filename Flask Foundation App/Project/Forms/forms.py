# CREATE FORMS HERE
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import IntegerField

class AddForm(FlaskForm):

    name = StringField('Kitten Name: ')
    submit = SubmitField('Add Kitten')

class DelForm(FlaskForm):

    id = IntegerField('Kitten ID: ')
    submit = SubmitField('Remove Kitten')

class AddOwnerForm(FlaskForm):

    name = StringField('Owner Name: ')
    kit_id = IntegerField('Kittend ID: ')
    submit = SubmitField('Add Owner')
