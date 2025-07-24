from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm, WorkoutForm, ProfileForm
from models import db, User, Workout
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fit-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Registered. Please login.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in!')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = WorkoutForm()
    if form.validate_on_submit():
        session['last_workout'] = form.workout_type.data
        workout = Workout(
            workout_type=form.workout_type.data,
            steps=form.steps.data,
            hours=form.hours.data,
            user_id=current_user.id
        )
        db.session.add(workout)
        db.session.commit()
        flash('Workout logged.')
        return redirect(url_for('history'))
    last_type = session.get('last_workout', 'None')
    return render_template('dashboard.html', form=form, last_type=last_type)

@app.route('/history')
@login_required
def history():
    logs = Workout.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', logs=logs)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        if check_password_hash(current_user.password, form.current_password.data):
            current_user.username = form.new_username.data
            if form.new_password.data:
                current_user.password = generate_password_hash(form.new_password.data)
            db.session.commit()
            flash('Profile updated.')
        else:
            flash('Current password incorrect.')
    return render_template('profile.html', form=form)

if __name__ == '__main__':
    with app.app_context():
         db.create_all() 
    app.run(debug=True)

