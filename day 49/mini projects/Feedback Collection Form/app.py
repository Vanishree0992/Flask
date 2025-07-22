from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email (optional)', validators=[Optional(), Email(message="Invalid email")])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, message="Message must be at least 10 characters")])
    submit = SubmitField('Submit Feedback')

@app.route('/', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        flash("Thank you for your feedback!", "success")
        return redirect(url_for('feedback'))
    return render_template('feedback.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
