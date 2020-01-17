from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField('Create UserName')
    password = PasswordField('Create Password')
    submit = SubmitField()