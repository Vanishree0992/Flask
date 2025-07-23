from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    event_name = db.Column(db.String(100), nullable=False)
