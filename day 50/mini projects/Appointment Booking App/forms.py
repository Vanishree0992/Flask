from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Time', validators=[DataRequired()])
    submit = SubmitField('Book Appointment')

class UpdateStatusForm(FlaskForm):
    status = SelectField('Update Status', choices=[
        ('pending', 'Pending'), 
        ('confirmed', 'Confirmed'), 
        ('canceled', 'Canceled')
    ], validators=[DataRequired()])
    submit = SubmitField('Update')
