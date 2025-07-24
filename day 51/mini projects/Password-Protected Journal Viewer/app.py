from flask import Flask, render_template, redirect, url_for, flash, request, session
from extensions import db, bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from db_models import User, JournalEntry
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'

db.init_app(app)
bcrypt.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=request.form['username'], password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            flash("Logged in successfully.")
            return redirect(url_for('dashboard'))
        flash("Invalid credentials.")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You’ve been logged out.")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    entries = JournalEntry.query.filter_by(user_id=current_user.id).order_by(JournalEntry.date_posted.desc()).all()
    return render_template('dashboard.html', entries=entries)

@app.route('/add', methods=['POST'])
@login_required
def add_entry():
    title = request.form['title']
    content = request.form['content']
    new_entry = JournalEntry(title=title, content=content, user_id=current_user.id)
    db.session.add(new_entry)
    db.session.commit()
    flash("Journal entry added.")
    return redirect(url_for('dashboard'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_entry(id):
    entry = JournalEntry.query.get_or_404(id)
    if entry.author != current_user:
        flash("Unauthorized access.")
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        entry.title = request.form['title']
        entry.content = request.form['content']
        db.session.commit()
        flash("Entry updated.")
        return redirect(url_for('dashboard'))
    return render_template('edit_entry.html', entry=entry)

@app.route('/delete/<int:id>')
@login_required
def delete_entry(id):
    entry = JournalEntry.query.get_or_404(id)
    if entry.author != current_user:
        flash("Unauthorized action.")
        return redirect(url_for('dashboard'))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted.")
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('journal.db'):
            db.create_all()
    app.run(debug=True)
