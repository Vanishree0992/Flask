from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Score
from forms import RegisterForm, LoginForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'quiz-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
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
            return redirect(url_for('dashboard'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    score = Score.query.filter_by(user_id=current_user.id).first()
    return render_template('dashboard.html', score=score)

@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "2 + 2 = ?": "4",
        "What is the color of the sky on a clear day?": "Blue"
    }

    if request.method == 'POST':
        correct = 0
        for question, answer in questions.items():
            user_answer = request.form.get(question)
            if user_answer and user_answer.strip().lower() == answer.lower():
                correct += 1
        # Save score to DB
        existing = Score.query.filter_by(user_id=current_user.id).first()
        if existing:
            existing.value = correct
        else:
            db.session.add(Score(user_id=current_user.id, value=correct))
        db.session.commit()
        flash(f'Quiz completed. You scored {correct}/{len(questions)}!')
        return redirect(url_for('results'))

    return render_template('quiz.html', questions=questions)

@app.route('/results')
@login_required
def results():
    score = Score.query.filter_by(user_id=current_user.id).first()
    return render_template('results.html', score=score)

if __name__ == '__main__':
    with app.app_context():
         db.create_all() 
    app.run(debug=True)