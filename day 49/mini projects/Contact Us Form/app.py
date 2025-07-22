from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=20, message="Message must be at least 20 characters")])
    submit = SubmitField("Send Message")

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Your message has been sent!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
