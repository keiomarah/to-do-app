from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import or_
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__, template_folder='.templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user: 
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Oops! Incorrect password. Please try again', category='failure')
        else:
            flash('Oops! Seems like that user does not exist. Please create an account.', category='failure')
    return render_template("login-signup.html", login=True)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        tp = bool(request.form.get('terms-and-privacy'))

        user = User.query.filter(
            or_(
                User.email == email,
                User.phone == phone
            )
        ).first()

        if user:
            flash('Sorry! User with that email or phone number already exists.', category='failure')
        elif len(name) < 2:
            print('flash working?')
            flash('Name must be longer than a character', category='failure')
        elif len(surname) < 2:
            flash('Surname must be longer than a character', category='failure')
        elif len(password1) < 8: 
            flash('Password must be at least 8 characters', category='failure')
        elif password1 != password2:
            flash('Oops! Passwords do not match', category='failure')
        elif (not tp):
            flash('Please agree to the terms and privacy', category='failure')
        else: 
            new_user = User(name=name, surname=surname, email=email, phone=phone, password=generate_password_hash(password1), tp=tp)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully', category='success')
            return redirect(url_for('views.home'))
        
    return render_template("login-signup.html", login=False)