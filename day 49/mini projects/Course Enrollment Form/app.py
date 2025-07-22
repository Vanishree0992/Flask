from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure value

class CourseEnrollmentForm(FlaskForm):
    name = StringField("Student Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    course = SelectField("Course", choices=[
        ("Python", "Python"),
        ("Java", "Java"),
        ("Web", "Web Development")
    ], validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=18, max=60, message="Age must be between 18 and 60")])
    submit = SubmitField("Enroll")

@app.route("/", methods=["GET", "POST"])
def enroll():
    form = CourseEnrollmentForm()
    if form.validate_on_submit():
        name = form.name.data
        course = form.course.data
        flash(f"Hi {name}, you enrolled in {course}")
        return redirect(url_for("success"))
    return render_template("enroll.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
