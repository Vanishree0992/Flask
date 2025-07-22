from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key'


DUMMY_EMAIL = "admin@example.com"
DUMMY_PASSWORD = "password123"


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Password must be at least 6 characters")])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == DUMMY_EMAIL and form.password.data == DUMMY_PASSWORD:
            flash("Login successful!", "success")
            return redirect(url_for('login'))
        else:
            flash("Invalid credentials", "error")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
