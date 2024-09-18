from  . import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

# Define the User and Profile models
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now())
    
    # Relationships
    profile = db.relationship('Profile', back_populates='user', uselist=False)  # One-to-One
    
    
class Profile(db.Model):
    __tablename__ = 'profile'
    profileid = db.Column(db.Integer, primary_key=True)  # Primary Key
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign Key
    user_preferences = db.Column(db.Text)
    movies_watched = db.Column(db.Text)
    updated_at = db.Column(db.DateTime(), default=datetime.now())


    # Relationship back to the User
    user = db.relationship('User', back_populates='profile')  # One-to-One

    # def last_seen(self):
    #     self.last_seen = datetime.now()
    #     db.session.add(self)
    #     db.session.commit()