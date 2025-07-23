from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired()])
    submit = SubmitField('Add Student')

class CourseForm(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired()])
    fee = IntegerField('Course Fee', validators=[DataRequired()])
    submit = SubmitField('Add Course')

class EnrollmentForm(FlaskForm):
    student_id = SelectField('Student', coerce=int)
    course_id = SelectField('Course', coerce=int)
    submit = SubmitField('Enroll')
