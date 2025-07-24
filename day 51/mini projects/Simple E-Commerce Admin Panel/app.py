from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Product
from forms import LoginForm, ProductForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def create_tables():
    if not hasattr(app, 'db_initialized'):
        if not User.query.filter_by(email='admin@example.com').first():
            admin = User(email='admin@example.com',
                         password=generate_password_hash('adminpass'))
            admin.is_admin = True
            db.session.add(admin)
            db.session.commit()
        app.db_initialized = True

@app.route('/')
def home():
    return redirect(url_for('products'))

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in as admin.' if user.is_admin else 'Logged in.')
            return redirect(url_for('products'))
        flash('Invalid credentials.')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

def admin_only(func):
    @login_required
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/product/add', methods=['GET','POST'])
@admin_only
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        p = Product(name=form.name.data, price=form.price.data, description=form.description.data)
        db.session.add(p)
        db.session.commit()
        flash('Product added.')
        return redirect(url_for('products'))
    return render_template('add_edit_product.html', form=form, action="Add")

@app.route('/product/edit/<int:id>', methods=['GET','POST'])
@admin_only
def edit_product(id):
    p = Product.query.get_or_404(id)
    form = ProductForm(obj=p)
    if form.validate_on_submit():
        form.populate_obj(p)
        db.session.commit()
        flash('Product updated.')
        return redirect(url_for('products'))
    return render_template('add_edit_product.html', form=form, action="Edit")

@app.route('/product/delete/<int:id>')
@admin_only
def delete_product(id):
    p = Product.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    flash('Product deleted.')
    return redirect(url_for('products'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
