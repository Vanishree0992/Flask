from flask import Flask, render_template, request, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

class LeaveForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])
    reason = TextAreaField("Reason for Leave", validators=[DataRequired()])
    start_date = DateField("Start Date", validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField("End Date", validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField("Apply")

@app.route("/", methods=["GET", "POST"])
def apply_leave():
    form = LeaveForm()
    if form.validate_on_submit():
        start = form.start_date.data
        end = form.end_date.data
        if end < start:
            form.end_date.errors.append("End date cannot be earlier than start date.")
        else:
            days = (end - start).days + 1
            flash(f"{form.name.data}, your leave from {start} to {end} ({days} days) was submitted.")
            return redirect(url_for("success"))
    return render_template("leave_form.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
