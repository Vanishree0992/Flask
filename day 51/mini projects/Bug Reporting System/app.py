from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, BugReport
from forms import RegisterForm, LoginForm, BugForm
from werkzeug.security import check_password_hash, generate_password_hash
import bcrypt
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bug-report-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.db'
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return redirect(url_for('my_bugs'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user.password.encode('utf-8')):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('my_bugs'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    form = BugForm()
    if form.validate_on_submit():
        bug = BugReport(title=form.title.data, description=form.description.data, user_id=current_user.id)
        db.session.add(bug)
        db.session.commit()
        session['last_bug_title'] = form.title.data
        flash('Bug submitted successfully.')
        return redirect(url_for('my_bugs'))
    return render_template('submit.html', form=form)

@app.route('/mybugs')
@login_required
def my_bugs():
    bugs = BugReport.query.filter_by(user_id=current_user.id).order_by(BugReport.id.desc()).all()
    last_bug = session.get('last_bug_title')
    return render_template('mybugs.html', bugs=bugs, last_bug=last_bug)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)