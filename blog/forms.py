from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    TextAreaField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,

)
from blog.models import User
from flask_login import current_user


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
                                                 EqualTo('password', message="password must match")])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username already exists")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email already exists")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(max=30, min=8),
                                                     ])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')


class UpdateProfileForm(FlaskForm):
    username = StringField('UserName',
                           validators=[DataRequired(),
                                       Length(min=8, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("This username already exists")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("This email already exists")

