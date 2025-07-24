from flask import Flask, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import bcrypt
from models import db, User, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'feedback-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect(url_for('feedback'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.hashpw(form.password.data.encode(), bcrypt.gensalt())
        user = User(username=form.username.data, password=hashed_pw, is_admin=False)
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
            return redirect(url_for('feedback'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('login'))

@app.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        fb = Feedback(user_id=current_user.id, message=form.message.data)
        db.session.add(fb)
        db.session.commit()
        flash("Thank you for your feedback!")
        return redirect(url_for('feedback'))
    return render_template('feedback.html', form=form)

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash("Admins only.")
        return redirect(url_for('feedback'))
    all_feedback = Feedback.query.all()
    return render_template('admin.html', feedbacks=all_feedback)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create default admin
        if not User.query.filter_by(username='admin').first():
            pw = bcrypt.hashpw('adminpass'.encode(), bcrypt.gensalt())
            db.session.add(User(username='admin', password=pw, is_admin=True))
            db.session.commit()
    app.run(debug=True)
