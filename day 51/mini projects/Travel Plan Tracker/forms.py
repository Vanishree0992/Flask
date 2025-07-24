from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class TravelPlanForm(FlaskForm):
    place = StringField('Place (Country)', validators=[InputRequired()])
    date = StringField('Date (YYYY-MM-DD)', validators=[InputRequired()])
    reason = StringField('Reason for Travel', validators=[InputRequired()])
    submit = SubmitField('Add Plan')

class SearchForm(FlaskForm):
    place = StringField('Search Country', validators=[InputRequired()])
    submit = SubmitField('Search')
