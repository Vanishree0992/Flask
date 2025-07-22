from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class BookingForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    room_type = SelectField('Room Type', choices=[
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite')
    ], validators=[DataRequired()])
    nights = IntegerField('Nights', validators=[DataRequired(), NumberRange(min=1, message="Must book at least 1 night")])
    submit = SubmitField('Book Now')

@app.route("/", methods=["GET", "POST"])
def book():
    form = BookingForm()
    if form.validate_on_submit():
        flash(f"Booking for {form.name.data} confirmed: {form.nights.data} nights in {form.room_type.data}")
        return redirect(url_for("success"))
    return render_template("booking.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
