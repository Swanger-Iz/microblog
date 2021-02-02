from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # Username field
    password = PasswordField('Password', validators=[DataRequired()]) # Password field
    remember_me = BooleanField('Remember Me') # Checkbutton
    submit = SubmitField('Sign In') # Sign in - button