from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(254), unique=True)
    enabled = db.Column(db.Boolean)

class group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
