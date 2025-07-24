from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Thread, Comment
from forms import RegisterForm, LoginForm, ThreadForm, CommentForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'forum-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@app.route('/')
def index():
    return redirect(url_for('threads'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash('Registered—please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u and check_password_hash(u.password, form.password.data):
            login_user(u)
            flash('Logged in.')
            return redirect(url_for('threads'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('login'))

@app.route('/threads')
@login_required
def threads():
    your_threads = Thread.query.filter_by(user_id=current_user.id).all()
    return render_template('threads.html', threads=your_threads)

@app.route('/thread/create', methods=['GET','POST'])
@login_required
def create_thread():
    form = ThreadForm()
    if form.validate_on_submit():
        t = Thread(title=form.title.data, body=form.body.data, user_id=current_user.id)
        db.session.add(t)
        db.session.commit()
        flash('Thread posted.')
        return redirect(url_for('threads'))
    return render_template('create_thread.html', form=form)

@app.route('/thread/<int:tid>', methods=['GET','POST'])
@login_required
def thread_detail(tid):
    thread = Thread.query.get_or_404(tid)
    if thread.user_id != current_user.id:
        flash("You can only view your own threads.")
        return redirect(url_for('threads'))
    form = CommentForm()
    if form.validate_on_submit():
        c = Comment(body=form.body.data, thread_id=tid, user_id=current_user.id)
        db.session.add(c)
        db.session.commit()
        flash('Comment added.')
        return redirect(url_for('thread_detail', tid=tid))
    return render_template('thread_detail.html', thread=thread, form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
