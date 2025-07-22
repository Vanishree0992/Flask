from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class BugReportForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    description = TextAreaField("Bug Description", validators=[DataRequired()])
    severity = RadioField("Severity", choices=[
        ('low', 'Low'), 
        ('medium', 'Medium'), 
        ('high', 'High')
    ], validators=[DataRequired()])
    submit = SubmitField("Submit Bug")

@app.route('/', methods=['GET', 'POST'])
def report():
    form = BugReportForm()
    if form.validate_on_submit():
        severity = form.severity.data
        if severity == 'high':
            flash("Thanks! We'll review this high severity bug ASAP.", "high")
        elif severity == 'medium':
            flash("Thanks! We’ll look into this medium severity issue soon.", "medium")
        else:
            flash("Thanks! We'll address this low priority bug when possible.", "low")
        return redirect(url_for('report'))
    return render_template('bug_report.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
