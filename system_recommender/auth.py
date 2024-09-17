from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User, Profile
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    #login code
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()

    # check if a user exists
    # take the user supplied password, hash it and compare to hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # If the user doesn't exist or password is wrong, reload the page
    
    # if the above check passes, then we know the user is in database
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database
    email = request.form.get('email')
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user: # if user is found, we want to redirect to a signup page
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so that the plain text version isn't saved
    new_user = User(email=email, name=name, username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))

    # add user to the database
    db.session.add(new_user)
    db.session.commit()

    # Create and associate a profile with the new user
    new_profile = Profile(id=new_user.id)
    db.session.add(new_profile)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))