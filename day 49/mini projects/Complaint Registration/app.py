from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import random

app = Flask(__name__)
app.secret_key = 'complaint_secret_key'

class ComplaintForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    category = SelectField("Category", choices=[
        ('service', 'Service Issue'),
        ('product', 'Product Defect'),
        ('billing', 'Billing Problem'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    complaint = TextAreaField("Complaint", validators=[DataRequired(), Length(min=15)])
    submit = SubmitField("Submit Complaint")

@app.route("/", methods=["GET", "POST"])
def complaint():
    form = ComplaintForm()
    if form.validate_on_submit():
        complaint_id = f"CMP{random.randint(1000, 9999)}"
        flash(f"Complaint submitted! Your ticket ID is {complaint_id}")
        return redirect(url_for("complaint"))
    return render_template("complaint.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
