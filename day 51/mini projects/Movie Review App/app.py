from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Review
from forms import RegisterForm, LoginForm, ReviewForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'movie-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
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
    return redirect(url_for('reviews'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('reviews'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/reviews')
def reviews():
    all_reviews = Review.query.order_by(Review.id.desc()).all()
    return render_template('reviews.html', reviews=all_reviews)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(user_id=current_user.id, rating=form.rating.data, comment=form.comment.data)
        db.session.add(review)
        db.session.commit()
        flash('Review submitted.')
        return redirect(url_for('reviews'))
    return render_template('add_review.html', form=form)

if __name__ == '__main__':
    with app.app_context():
         db.create_all() 
    app.run(debug=True)