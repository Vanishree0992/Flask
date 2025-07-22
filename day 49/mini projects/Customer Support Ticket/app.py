from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import random

app = Flask(__name__)
app.secret_key = 'support_secret_key'

class TicketForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    category = SelectField('Issue Category', choices=[
        ('Billing', 'Billing'),
        ('Technical', 'Technical'),
        ('Account', 'Account'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=25, message="Description must be at least 25 characters")])
    submit = SubmitField('Submit Ticket')

@app.route("/", methods=["GET", "POST"])
def ticket():
    form = TicketForm()
    if form.validate_on_submit():
        ticket_id = f"TKT{random.randint(1000, 9999)}"
        flash(f"Support ticket submitted! Your Ticket ID is {ticket_id}")
        return redirect(url_for('success'))
    return render_template("ticket.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
