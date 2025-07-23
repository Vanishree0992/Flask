from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, Employee
from forms import EmployeeForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        emp = Employee(
            name=form.name.data,
            position=form.position.data,
            department=form.department.data,
            salary=form.salary.data
        )
        db.session.add(emp)
        db.session.commit()
        flash("Employee added!", "success")
        return redirect(url_for('add_employee'))
    return render_template('add.html', form=form)

@app.route('/employees')
def view_employees():
    dept = request.args.get('department')
    if dept:
        employees = Employee.query.filter_by(department=dept).all()
    else:
        employees = Employee.query.all()
    return render_template('view.html', employees=employees)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    emp = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=emp)
    if form.validate_on_submit():
        emp.name = form.name.data
        emp.position = form.position.data
        emp.department = form.department.data
        emp.salary = form.salary.data
        db.session.commit()
        flash("Employee updated!", "info")
        return redirect(url_for('view_employees'))
    return render_template('update.html', form=form)

@app.route('/delete/<int:id>')
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    flash("Employee deleted!", "danger")
    return redirect(url_for('view_employees'))

if __name__ == '__main__':
    app.run(debug=True)
