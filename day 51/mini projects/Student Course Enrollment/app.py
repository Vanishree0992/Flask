from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Course, Enrollment
from forms import RegisterForm, LoginForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'courses-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect(url_for('courses'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u and check_password_hash(u.password, form.password.data):
            login_user(u)
            flash('Logged in.')
            return redirect(url_for('courses'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/courses')
@login_required
def courses():
    all_courses = Course.query.all()
    enrolled_ids = {e.course_id for e in current_user.enrollments}
    return render_template('courses.html', courses=all_courses, enrolled=enrolled_ids)

@app.route('/enroll/<int:cid>')
@login_required
def enroll(cid):
    if not Enrollment.query.filter_by(user_id=current_user.id, course_id=cid).first():
        e = Enrollment(user_id=current_user.id, course_id=cid)
        db.session.add(e)
        db.session.commit()
        flash('Enrolled successfully!')
    else:
        flash('Already enrolled.')
    return redirect(url_for('courses'))

@app.route('/history')
@login_required
def history():
    return render_template('history.html', enrollments=current_user.enrollments)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if Course.query.count() == 0:
            for title in ['Math 101','History 201','Science 301']:
                db.session.add(Course(title=title))
            db.session.commit()
    app.run(debug=True)
