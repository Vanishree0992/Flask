from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.secret_key = "feedback_secret"

class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    course = StringField("Course", validators=[DataRequired()])
    rating = IntegerField("Rating (1–10)", validators=[DataRequired(), NumberRange(min=1, max=10)])
    suggestion = TextAreaField("Suggestion (Optional)")
    submit = SubmitField("Submit Feedback")

@app.route("/", methods=["GET", "POST"])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        rating = form.rating.data
        if rating < 5:
            flash("Thanks for your feedback. We'll improve!")
        elif rating < 8:
            flash("Thanks! We're glad you found it useful.")
        else:
            flash("Awesome! Thanks for the high rating!")
        return redirect(url_for("thankyou"))
    return render_template("feedback.html", form=form)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
