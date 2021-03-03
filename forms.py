from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField,TextAreaField
from flask_wtf.file import FileField, FileRequired,FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                                     validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                               validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                                        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user: 
            raise ValidationError('That username is taken. Please choose another one')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user: 
            raise ValidationError('That email is taken. Please choose another one')

    def validate_password(self, password):
        if len(password.data) < 5:
            raise ValidationError('Weak')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                                     validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                               validators=[DataRequired(), Email()])


    submit = SubmitField('Update')
    picture = FileField('Update Profile Pic',
                                                validators=[FileAllowed(['jpg','png','jpeg'])])

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user: 
                raise ValidationError('That username is taken. Please choose another one')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user: 
                raise ValidationError('That email is taken. Please choose another one')


class LoginForm(FlaskForm):
    email = StringField('Email',
                               validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                                validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None: 
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                                        validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Reset Password')                                                   