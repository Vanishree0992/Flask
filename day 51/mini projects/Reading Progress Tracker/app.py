from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Book
from forms import RegisterForm, LoginForm, BookForm, ProgressForm
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'reading-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reading.db'
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
        flash('Registered successfully! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode(), user.password):
            login_user(user)
            session['last_book'] = None
            flash('Welcome back!')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash("You’ve been logged out.")
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, total_pages=form.total_pages.data, user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        flash('Book added!')
        return redirect(url_for('dashboard'))
    books = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', form=form, books=books, last_book=session.get('last_book'))

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    if book.user_id != current_user.id:
        flash("Access denied.")
        return redirect(url_for('dashboard'))
    session['last_book'] = book.title
    form = ProgressForm(pages_read=book.pages_read)
    if form.validate_on_submit():
        if 0 <= form.pages_read.data <= book.total_pages:
            book.pages_read = form.pages_read.data
            db.session.commit()
            flash('Progress updated!')
        else:
            flash('Invalid page number.')
        return redirect(url_for('book_detail', book_id=book_id))
    return render_template('book_detail.html', book=book, form=form)
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
