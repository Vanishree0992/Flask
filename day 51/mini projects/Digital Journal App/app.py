from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

from models import db, User, Entry
from forms import RegisterForm, LoginForm, EntryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'journal-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect(url_for('journal'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
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
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            session['login_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            flash('Logged in successfully.')
            return redirect(url_for('journal'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/journal')
@login_required
def journal():
    entries = Entry.query.filter_by(user_id=current_user.id).order_by(Entry.id.desc()).all()
    return render_template('journal.html', entries=entries, login_time=session.get('login_time'))

@app.route('/entry/add', methods=['GET', 'POST'])
@login_required
def add_entry():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(entry)
        db.session.commit()
        flash('Entry added.')
        return redirect(url_for('journal'))
    return render_template('add_edit.html', form=form, action="Add")

@app.route('/entry/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_entry(id):
    entry = Entry.query.get_or_404(id)
    if entry.user_id != current_user.id:
        flash("You can't edit others' entries.")
        return redirect(url_for('journal'))
    form = EntryForm(obj=entry)
    if form.validate_on_submit():
        entry.title = form.title.data
        entry.content = form.content.data
        db.session.commit()
        flash('Entry updated.')
        return redirect(url_for('journal'))
    return render_template('add_edit.html', form=form, action="Edit")

@app.route('/entry/delete/<int:id>')
@login_required
def delete_entry(id):
    entry = Entry.query.get_or_404(id)
    if entry.user_id != current_user.id:
        flash("You can't delete others' entries.")
        return redirect(url_for('journal'))
    db.session.delete(entry)
    db.session.commit()
    flash('Entry deleted.')
    return redirect(url_for('journal'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
