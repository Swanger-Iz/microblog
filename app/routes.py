# -*- coding: utf-8 -*-

from flask import render_template
from app import app

@app.route('/')
@app.route('/index/')
def index():
    user = {'name': 'ilgiz'}
    posts = [
        {
            'author': {'username': 'Eldar Ryazanov'},
            'body': 'Welcome to the Porthland'
        },
        {
            'author': {'username': 'Gachi Muchi'},
            'body': 'Boy next door'
        },
        {
            'author': {'username': 'Billy Harrington'},
            'body': 'F\'in slaveee'
        },
        {
            'author': {'username': 'Sergey Pozdnyak'},
            'body': 'EEEE boiii'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


