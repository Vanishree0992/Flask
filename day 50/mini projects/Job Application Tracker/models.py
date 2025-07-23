from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Applied')
