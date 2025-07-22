from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'supersecretkey'

class RSVPForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    will_attend = BooleanField("I will attend the event")
    submit = SubmitField("Submit RSVP")

@app.route('/', methods=['GET', 'POST'])
def rsvp():
    form = RSVPForm()
    if form.validate_on_submit():
        if form.will_attend.data:
            flash("Thanks for RSVPing!", "success")
        else:
            flash("Sorry to miss you", "warning")
        return redirect(url_for('rsvp'))
    return render_template('rsvp.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
