from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, URL, NumberRange

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

class JobApplicationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    resume = StringField("Resume URL", validators=[DataRequired(), URL()])
    experience = IntegerField("Years of Experience", validators=[DataRequired(), NumberRange(min=0, message="Experience must be 0 or more")])
    submit = SubmitField("Apply")

@app.route("/", methods=["GET", "POST"])
def apply():
    form = JobApplicationForm()
    if form.validate_on_submit():
        flash(f"{form.name.data}, your job application has been received.")
        return redirect(url_for("success"))
    return render_template("apply.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
