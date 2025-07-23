from flask import Flask, render_template, redirect, url_for, flash
from datetime import datetime, date, time
from config import Config
from models import db, Appointment
from forms import AppointmentForm, UpdateStatusForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def book():
    form = AppointmentForm()
    if form.validate_on_submit():
        appointment = Appointment(
            name=form.name.data,
            date=form.date.data,
            time=form.time.data,
            status='pending'
        )
        db.session.add(appointment)
        db.session.commit()
        flash("Appointment booked!", "success")
        return redirect(url_for('book'))
    return render_template('book.html', form=form)

@app.route('/appointments')
def appointments():
    all_appointments = Appointment.query.order_by(Appointment.date, Appointment.time).all()
    return render_template('appointments.html', appointments=all_appointments)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    appointment = Appointment.query.get_or_404(id)
    form = UpdateStatusForm(status=appointment.status)
    if form.validate_on_submit():
        appointment.status = form.status.data
        db.session.commit()
        flash("Status updated!", "info")
        return redirect(url_for('appointments'))
    return render_template('update.html', form=form, appointment=appointment)

@app.route('/delete_expired')
def delete_expired():
    now = datetime.now()
    expired = Appointment.query.filter(
        (Appointment.date < date.today()) |
        ((Appointment.date == date.today()) & (Appointment.time < now.time()))
    ).all()
    for a in expired:
        db.session.delete(a)
    db.session.commit()
    flash(f"{len(expired)} expired appointments deleted.")
    return redirect(url_for('appointments'))

if __name__ == '__main__':
    app.run(debug=True)
