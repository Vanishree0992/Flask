from flask import render_template, redirect, url_for, flash
from . import db
from .models import User
from .forms import UserForm
from flask import current_app as app

@app.route('/')
def index():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        try:
            user = User(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {e}', 'danger')
    return render_template('add_user.html', form=form)
