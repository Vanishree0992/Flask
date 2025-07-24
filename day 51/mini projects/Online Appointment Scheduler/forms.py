from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class AppointmentForm(FlaskForm):
    date = StringField('Date (YYYY-MM-DD)', validators=[InputRequired()])
    time = StringField('Time (HH:MM)', validators=[InputRequired()])
    reason = StringField('Reason', validators=[InputRequired()])
    submit = SubmitField('Submit')
