from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, Attendee
from forms import AttendeeForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def register():
    form = AttendeeForm()
    if form.validate_on_submit():
        attendee = Attendee(
            name=form.name.data,
            email=form.email.data,
            event_name=form.event_name.data
        )
        db.session.add(attendee)
        db.session.commit()
        flash("Attendee registered successfully!", "success")
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

@app.route('/attendees')
def attendees():
    all_attendees = Attendee.query.all()
    return render_template('attendees.html', attendees=all_attendees)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_attendee(id):
    attendee = Attendee.query.get_or_404(id)
    form = AttendeeForm(obj=attendee)
    if form.validate_on_submit():
        attendee.name = form.name.data
        attendee.email = form.email.data
        attendee.event_name = form.event_name.data
        db.session.commit()
        flash("Attendee updated!", "info")
        return redirect(url_for('attendees'))
    return render_template('edit_attendee.html', form=form)

@app.route('/delete/<int:id>')
def delete_attendee(id):
    attendee = Attendee.query.get_or_404(id)
    db.session.delete(attendee)
    db.session.commit()
    flash("Attendee deleted!", "danger")
    return redirect(url_for('attendees'))

if __name__ == '__main__':
    app.run(debug=True)
