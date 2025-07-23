from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class SubscriptionForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    plan = SelectField("Plan", choices=[("Free", "Free"), ("Pro", "Pro"), ("Enterprise", "Enterprise")], validators=[DataRequired()])
    submit = SubmitField("Subscribe")
