from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class Register(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])#To get the mail id
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8,max=15)])
    conform_password=PasswordField('Conform_Password',validators=[DataRequired(),EqualTo('password')])
    sign=SubmitField('SignUp')

class Login(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])#To get the mail id
    password=PasswordField('Password',validators=[DataRequired()])
    sign=SubmitField('SignIn')

class Admin(FlaskForm):
    userid=StringField('UserID',validators=[DataRequired(),Length(min=8,max=15)])#To get the mail id
    password=PasswordField('Password',validators=[DataRequired()])
    sign=SubmitField('SignIn')