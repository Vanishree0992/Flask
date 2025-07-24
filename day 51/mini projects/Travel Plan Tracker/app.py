from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, TravelPlan
from forms import RegisterForm, LoginForm, TravelPlanForm, SearchForm
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'travel-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode(), user.password):
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = TravelPlanForm()
    if form.validate_on_submit():
        plan = TravelPlan(
            user_id=current_user.id,
            place=form.place.data,
            date=form.date.data,
            reason=form.reason.data
        )
        db.session.add(plan)
        db.session.commit()
        flash('Travel plan added!')
        return redirect(url_for('dashboard'))
    
    plans = TravelPlan.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', form=form, plans=plans, total=len(plans))

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    results = []
    if form.validate_on_submit():
        country = form.place.data
        session['last_search'] = country
        results = TravelPlan.query.filter_by(user_id=current_user.id, place=country).all()
    return render_template('search.html', form=form, results=results, last=session.get('last_search'))
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
