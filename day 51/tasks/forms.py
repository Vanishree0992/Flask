from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(),Length(min=4,max=150)])
    email = StringField('Email',validators=[InputRequired(),Email()])
    Password = PasswordField('username',validators=[InputRequired(),Length(min=6)])
    confirm_Password = PasswordField('username',validators=[InputRequired(),EqualTo('password')])

submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired()])
    Password = PasswordField('username',validators=[InputRequired()])
   
submit = SubmitField('Register')