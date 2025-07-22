from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.secret_key = 'donation_secret_key'

class DonationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    amount = IntegerField("Amount", validators=[DataRequired(), NumberRange(min=10, message="Minimum donation is $10")])
    cause = SelectField("Cause", choices=[
        ('education', 'Education'),
        ('health', 'Health'),
        ('environment', 'Environment'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    submit = SubmitField("Donate")

@app.route("/", methods=["GET", "POST"])
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        flash(f"Thank you {form.name.data}, you donated ${form.amount.data} towards {form.cause.data.capitalize()}.")
        return redirect(url_for("donate"))
    return render_template("donation.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
