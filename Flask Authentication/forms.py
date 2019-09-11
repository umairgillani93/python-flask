# forms.py
from flask import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class Login(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(),Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired(), EqualTo('pass_confirm', message = 'Passwords mush match!')])
    pass_confirm = PasswordField('Confim Password', validators = [DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Your Email already registered!')

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already taken!')
