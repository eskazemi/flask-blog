from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    PasswordField,
    BooleanField, 
    SubmitField,
    )
from wtforms.validators import (
    DataRequired, 
    Length, 
    Email, 
    EqualTo,
    )


class RegistrationForm(FlaskForm):
    username = StringField('UserName',
                           validators=[DataRequired(),
                                       Length(min=8, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(max=30, min=8),
                                                     ])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(max=30, min=8),
                                                     ])
    remember = BooleanField("Remember Me")