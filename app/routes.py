from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Justin'}
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
    return render_template('index.html', title='MyDataConsulting', user=user, posts=posts)
