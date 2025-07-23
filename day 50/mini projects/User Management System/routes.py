
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.order_by(User.joined_on.desc()).all()
    return render_template('index.html', users=users)

@main.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_user.html')

@main.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.password = request.form['password']
        db.session.commit()
        flash('User updated successfully!', 'info')
        return redirect(url_for('main.index'))
    return render_template('edit_user.html', user=user)

@main.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted.', 'danger')
    return redirect(url_for('main.index'))
