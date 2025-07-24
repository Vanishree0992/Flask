from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class ApplicationForm(FlaskForm):
    job_title = StringField('Job Title', validators=[InputRequired()])
    company = StringField('Company Name', validators=[InputRequired()])
    resume = TextAreaField('Resume Details', validators=[InputRequired(), Length(min=10)])
    submit = SubmitField('Apply')
