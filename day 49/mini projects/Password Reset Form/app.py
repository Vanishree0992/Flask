from flask import Flask, render_template, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)
app.secret_key = 'reset_secret'

class PasswordResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("New Password", validators=[DataRequired()])
    confirm = PasswordField("Confirm Password", validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField("Reset Password")

@app.route("/", methods=["GET", "POST"])
def reset():
    form = PasswordResetForm()
    if form.validate_on_submit():
        flash("Your password has been reset successfully!")
        return redirect(url_for("reset"))
    return render_template("reset.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
