from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

# ...

# everything here referred to as "view functions"

@app.route('/')
@app.route('/index')
@login_required # redirect anon user back to login page.
def index():
    posts = [
        {
            'author': {'username':'Justin'},
            'body': 'Beautiful day Portland!'
        },
        {
            'author': {'username':'Susan'},
            'body': 'The Avengers movie was so cool!' 
        },
        {
            'author': {'username':'Smitty'},
            'body': 'The sun will come out tomorrow!'
        }
    ]
    return render_template('index.html', title='MyDataConsulting', posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>') #using dynamic component <>
@login_required # only make the profile available to logged in user.
def user(username):
    user = User.query.filter_by(username = username).first_or_404()
    posts = [
        {'author':user, 'body':'Test post #1'},
        {'author': user, 'body':'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)