from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo


#Registration

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[InputRequired('Username required'), Length(min=5, max=20, message='Must be between 5 and 20 characters long')])
    email = StringField('Email',
                            validators=[InputRequired('Email required'), Email('Invalid email address')])
    password = PasswordField('Password',
                            validators=[InputRequired(message='Password required'), Length(min=8, max=20, message='Must be between 8 and 20 characters long')])
    confirm_password = PasswordField('Confirm Password',
                            validators=[InputRequired(message='Confirm password'), EqualTo('password', message='Passwords do not match')])
    submit = SubmitField('Sign Up')

#Login

class LoginForm(FlaskForm):
    email = StringField('Email',
                            validators=[InputRequired('Email required'), Email('Invalid email address')])
    password = PasswordField('Password',
                            validators=[InputRequired(message='Password required')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
