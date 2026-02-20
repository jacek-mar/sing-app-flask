"""Flask Sing App - Admin Forms"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional


class UserForm(FlaskForm):
    """Create or edit a user."""
    username = StringField('Username', validators=[DataRequired(), Length(2, 80)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password',
        validators=[Optional(), Length(min=8)],
        description='Leave blank to keep the existing password.'
    )
    is_admin = BooleanField('Admin')
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save')
