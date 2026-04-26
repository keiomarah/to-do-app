from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__, template_folder='.templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login-signup.html", login=True)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        tp = request.form.get('terms-and-privacy')

        if len(name) < 2:
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
            flash('Account created successfully', category='success')
        
    return render_template("login-signup.html", login=False)