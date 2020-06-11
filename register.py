from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import Form


class signUpForm(Form):
    name_first = StringField('User Name', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')