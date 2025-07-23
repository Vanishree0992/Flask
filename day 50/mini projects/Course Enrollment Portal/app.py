from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Student, Course, Enrollment
from forms import StudentForm, CourseForm, EnrollmentForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data)
        db.session.add(student)
        db.session.commit()
        flash('Student added!')
        return redirect(url_for('add_student'))
    return render_template('add_student.html', form=form)

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(name=form.name.data, fee=form.fee.data)
        db.session.add(course)
        db.session.commit()
        flash('Course added!')
        return redirect(url_for('add_course'))
    return render_template('add_course.html', form=form)

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    form = EnrollmentForm()
    form.student_id.choices = [(s.id, s.name) for s in Student.query.all()]
    form.course_id.choices = [(c.id, c.name) for c in Course.query.all()]
    if form.validate_on_submit():
        enrollment = Enrollment(student_id=form.student_id.data, course_id=form.course_id.data)
        db.session.add(enrollment)
        db.session.commit()
        flash('Enrollment successful!')
        return redirect(url_for('list_enrollments'))
    return render_template('enroll.html', form=form)

@app.route('/')
@app.route('/enrollments')
def list_enrollments():
    enrollments = Enrollment.query.all()
    return render_template('list_enrollments.html', enrollments=enrollments)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_enrollment(id):
    enrollment = Enrollment.query.get_or_404(id)
    form = EnrollmentForm(obj=enrollment)
    form.student_id.choices = [(s.id, s.name) for s in Student.query.all()]
    form.course_id.choices = [(c.id, c.name) for c in Course.query.all()]
    if form.validate_on_submit():
        enrollment.student_id = form.student_id.data
        enrollment.course_id = form.course_id.data
        db.session.commit()
        flash('Enrollment updated!')
        return redirect(url_for('list_enrollments'))
    return render_template('update_enrollment.html', form=form)

@app.route('/delete/<int:id>')
def delete_enrollment(id):
    enrollment = Enrollment.query.get_or_404(id)
    db.session.delete(enrollment)
    db.session.commit()
    flash('Enrollment deleted.')
    return redirect(url_for('list_enrollments'))

if __name__ == '__main__':
    app.run(debug=True)
