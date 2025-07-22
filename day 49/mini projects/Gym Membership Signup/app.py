from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, InputRequired

app = Flask(__name__)
app.secret_key = 'gym_secret_key'

class GymSignupForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=16, message="Must be at least 16 years old")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    plan = SelectField("Plan", choices=[('monthly', 'Monthly'), ('yearly', 'Yearly')], validators=[InputRequired()])
    accept_terms = BooleanField("I accept the Terms and Conditions", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

@app.route("/", methods=["GET", "POST"])
def signup():
    form = GymSignupForm()
    if form.validate_on_submit():
        flash(f"Welcome to our gym, {form.name.data}!")
        return redirect(url_for("signup"))
    return render_template("signup.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
