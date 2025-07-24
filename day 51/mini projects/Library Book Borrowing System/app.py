from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import bcrypt
import os
from models import db, User, Book, Borrow
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lib-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route('/')
def homepage():
    return redirect(url_for('catalog'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pw = bcrypt.hashpw(form.password.data.encode(), bcrypt.gensalt())
        user = User(username=form.username.data, password=pw, is_admin=False)
        db.session.add(user)
        db.session.commit()
        flash('Registered! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode(), user.password):
            login_user(user)
            session['recent'] = []
            flash('Logged in!')
            return redirect(url_for('catalog'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash("You've been logged out.")
    return redirect(url_for('login'))

@app.route('/catalog')
@login_required
def catalog():
    books = Book.query.all()
    return render_template('catalog.html', books=books, recent=session.get('recent', []))

@app.route('/borrow/<int:bid>')
@login_required
def borrow(bid):
    book = Book.query.get_or_404(bid)
    if not Borrow.query.filter_by(user_id=current_user.id, book_id=bid).first():
        borrow = Borrow(user_id=current_user.id, book_id=bid)
        db.session.add(borrow)
        db.session.commit()
        session.setdefault('recent', []).insert(0, book.title)
        session['recent'] = session['recent'][:5]
        flash(f'You borrowed "{book.title}".')
    else:
        flash('Already borrowed.')
    return redirect(url_for('catalog'))

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('Admin only.')
        return redirect(url_for('catalog'))
    borrows = Borrow.query.all()
    return render_template('admin.html', borrows=borrows)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            pw = bcrypt.hashpw('adminpass'.encode(), bcrypt.gensalt())
            db.session.add(User(username='admin', password=pw, is_admin=True))
        default_books = ['1984', 'Brave New World', 'Fahrenheit 451']
        if Book.query.count() == 0:
            [db.session.add(Book(title=b)) for b in default_books]
        db.session.commit()
    app.run(debug=True)
