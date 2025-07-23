from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class ApplicationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Applied', 'Applied'), ('Shortlisted', 'Shortlisted'), ('Rejected', 'Rejected')])
    submit = SubmitField('Submit')

class StatusForm(FlaskForm):
    status = SelectField('Status', choices=[('Applied', 'Applied'), ('Shortlisted', 'Shortlisted'), ('Rejected', 'Rejected')])
    submit = SubmitField('Update Status')
