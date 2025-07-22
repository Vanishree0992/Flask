from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, BooleanField, PasswordField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, Optional, Regexp, ValidationError

# 2.11 – Custom validator to block test.com emails
def block_test_domain(form, field):
    if field.data.endswith("@test.com"):
        raise ValidationError("Emails from test.com are not allowed.")

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(message="Name is required."),
        Length(min=3, message="Name must be at least 3 characters."),
        Regexp(r'^[A-Za-z ]+$', message="Only letters allowed.")
    ])
    email = StringField("Email", validators=[
        DataRequired(), Email(), block_test_domain
    ])
    password = PasswordField("Password", validators=[
        DataRequired(), Length(min=6)
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(), EqualTo('password', message="Passwords must match.")
    ])
    message = TextAreaField("Message", validators=[Optional()])
    gender = RadioField("Gender", choices=[('M', 'Male'), ('F', 'Female')], validators=[DataRequired()])
    country = SelectField("Country", choices=[('', 'Choose...'), ('in', 'India'), ('us', 'USA')], validators=[DataRequired()])
    accept_terms = BooleanField("I accept the terms", validators=[DataRequired(message="You must accept the terms.")])
    birthdate = DateField("Birth Date", format='%Y-%m-%d', validators=[Optional()])
    age = IntegerField("Age", validators=[
        DataRequired(), NumberRange(min=18, max=60, message="Age must be between 18 and 60.")
    ])
    submit = SubmitField("Submit")
