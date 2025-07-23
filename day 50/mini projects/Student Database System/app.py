# app.py
from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, Student
from forms import StudentForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    students = Student.query.order_by(Student.id.desc()).all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            name=form.name.data,
            roll_no=form.roll_no.data,
            email=form.email.data,
            age=form.age.data
        )
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_student.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.name = form.name.data
        student.roll_no = form.roll_no.data
        student.email = form.email.data
        student.age = form.age.data
        db.session.commit()
        flash('Student updated successfully!', 'info')
        return redirect(url_for('index'))
    return render_template('edit_student.html', form=form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted.', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
