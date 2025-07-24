from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from models import db, User, Appointment
from forms import RegisterForm, LoginForm, AppointmentForm
import bcrypt
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'appt-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.hashpw(form.password.data.encode(), bcrypt.gensalt())
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Registered! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode(), user.password):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', appointments=appointments)

@app.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    form = AppointmentForm()
    if form.validate_on_submit():
        appt = Appointment(user_id=current_user.id,
                           date=form.date.data,
                           time=form.time.data,
                           reason=form.reason.data)
        db.session.add(appt)
        db.session.commit()
        flash('Appointment booked.')
        return redirect(url_for('dashboard'))
    return render_template('update.html', form=form, title='Book Appointment')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    appt = Appointment.query.get_or_404(id)
    if appt.user_id != current_user.id:
        flash("Unauthorized.")
        return redirect(url_for('dashboard'))

    form = AppointmentForm(obj=appt)
    if form.validate_on_submit():
        appt.date = form.date.data
        appt.time = form.time.data
        appt.reason = form.reason.data
        db.session.commit()
        flash('Appointment updated.')
        return redirect(url_for('dashboard'))

    return render_template('update.html', form=form, title='Update Appointment')

@app.route('/cancel/<int:id>')
@login_required
def cancel(id):
    appt = Appointment.query.get_or_404(id)
    if appt.user_id != current_user.id:
        flash("Unauthorized.")
        return redirect(url_for('dashboard'))
    db.session.delete(appt)
    db.session.commit()
    flash('Appointment cancelled.')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
