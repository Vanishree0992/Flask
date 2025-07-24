from flask import Flask, render_template, redirect, url_for, flash, session, request
from extensions import db, bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime
import os

from models import User, Event, RSVP  # renamed import

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rsvp.db'

db.init_app(app)
bcrypt.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# (Keep all routes the same as before...)

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('rsvp.db'):
            db.create_all()
            db.session.add_all([
                Event(name='Music Concert', date=datetime(2025, 8, 15)),
                Event(name='Tech Meetup', date=datetime(2025, 9, 1)),
                Event(name='Art Festival', date=datetime(2025, 10, 10))
            ])
            db.session.commit()
    app.run(debug=True)
