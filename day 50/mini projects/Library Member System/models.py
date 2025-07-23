from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_date = db.Column(db.Date, default=date.today)
