from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.secret_key = "survey_secret"

class SurveyForm(FlaskForm):
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=18, max=100)])
    gender = RadioField("Gender", choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")], validators=[DataRequired()])
    product = SelectField("Favorite Product", choices=[("Laptop", "Laptop"), ("Phone", "Phone"), ("Tablet", "Tablet")], validators=[DataRequired()])
    feedback = TextAreaField("Feedback", validators=[DataRequired()])
    submit = SubmitField("Submit Survey")

@app.route("/", methods=["GET", "POST"])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        flash("Thanks for participating!")
        return redirect(url_for("thankyou"))
    return render_template("survey.html", form=form)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
