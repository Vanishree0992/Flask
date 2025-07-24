from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import bcrypt
from models import db, User, JobApplication
from forms import RegisterForm, LoginForm, ApplicationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'job-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route('/')
def home():
    return redirect(url_for('apply'))

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
            flash('Logged in successfully!')
            return redirect(url_for('apply'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('login'))

@app.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
    form = ApplicationForm()
    if form.validate_on_submit():
        appn = JobApplication(
            user_id=current_user.id,
            job_title=form.job_title.data,
            company=form.company.data,
            resume=form.resume.data
        )
        db.session.add(appn)
        db.session.commit()
        flash('Application submitted successfully!')
        return redirect(url_for('my_applications'))
    return render_template('apply.html', form=form)

@app.route('/my-applications')
@login_required
def my_applications():
    apps = JobApplication.query.filter_by(user_id=current_user.id).all()
    return render_template('my_applications.html', apps=apps)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
