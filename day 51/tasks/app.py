from flask import Flask, render_template, redirect, url_for, request, flash 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, UserMixin, login_user, logout_user,login_required, current_user 
from models import db,User
from forms import RegistrationForm,LoginForm
from flask_bcrypt import Bcrypt

app = Flask(__name__) 

app.config["SECRET_KEY"] = "mysecret" 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" 
 
db.init_app(app)

bcrypt = Bcrypt(app) 

login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view = "login" 
 
 
@login_manager.user_loader 
def load_user(user_id): 
    return User.query.get(int(user_id)) 
 
@app.route("/register", methods=["GET", "POST"]) 
def register(): 
     form = RegistrationForm()
     if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8') 
 
        user = User(username=form.username.data,email=form.email.data, password=hashed_pw) 
        db.session.add(user) 
        db.session.commit() 
        flash("Registration successful! Please login.", "success") 
        return redirect(url_for("login")) 
 
     return render_template('register.html',form=form) 
 
@app.route("/login", methods=["GET", "POST"]) 
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
     user = user.query.filter_by(username=form.username.data).first()
     if user and bcrypt.check_password_hash(user.password,form.Password.data):
         login_user(user)
         return render_template("home") 
     else:
        flash('login unsuccessful')
 
     return render_template('register.html',form=form) 
 
@app.route("/dashboard") 
@login_required 
def dashboard(): 
    return render_template ('dashboard.html',username=current_user.username) 
 
@app.route("/logout") 
@login_required 
def logout(): 
    logout_user() 
    return redirect(url_for("login")) 
 

@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html',username=current_user.username)
    else:
        return render_template('index.html',username=None)

@app.route('/all_users')
@login_required
def all_users():
     users = User.query.all()
     return render_template('all_usrs.html',user=users)


if __name__ == "__main__": 
    with app.app_context():
         db.create_all() 
    app.run(debug=True)