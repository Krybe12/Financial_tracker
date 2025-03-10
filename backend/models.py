from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False, unique=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now()) 