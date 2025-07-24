from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class BookForm(FlaskForm):
    title = StringField('Book Title', validators=[InputRequired()])
    total_pages = IntegerField('Total Pages', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Add Book')

class ProgressForm(FlaskForm):
    pages_read = IntegerField('Pages Read', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Update Progress')
