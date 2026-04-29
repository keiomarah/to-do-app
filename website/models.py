from . import db
from flask_login import UserMixin
from datetime import date
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    phone = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150))
    tp = db.Column(db.Boolean, default=False)
    tasks = db.relationship('Task')


class Task(db.Model):
    task_name = db.Column(db.String(1000))
    complete = db.Column(db.Boolean, default=False)
    due = db.Column(db.Date, default=func.now())
    priority = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


