from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    date = DateField("Date", validators=[DataRequired()], format='%Y-%m-%d')
    time = TimeField("Time", validators=[DataRequired()], format='%H:%M')
    purpose = TextAreaField("Purpose", validators=[DataRequired()])
    submit = SubmitField("Book Appointment")

@app.route("/", methods=["GET", "POST"])
def book():
    form = AppointmentForm()
    if form.validate_on_submit():
        flash(f"Appointment booked for {form.date.data.strftime('%Y-%m-%d')} at {form.time.data.strftime('%H:%M')}")
        return redirect(url_for("success"))
    return render_template("book.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
