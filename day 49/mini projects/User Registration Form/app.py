from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session & flash

# --- Flask-WTF Registration Form ---
class RegistrationForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

# --- Route for Registration ---
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Welcome, {form.fullname.data}! Registration successful.", "success")
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
