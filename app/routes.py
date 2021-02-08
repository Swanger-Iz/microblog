# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index/')
@login_required
def index():
    user = {'username': 'ilgiz'}
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

# methods=['GET', 'POST'] - форма отправляет браузеру только пост запросы, а на сервер отправляет пост запросы
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # Логи
    print(form.username.data, form.password.data, form.remember_me.data)
    # form.validate_on_submit()
    # 1. Запускает все варидаторы (форму ввода пользователя, пароля и т.д.)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        #if
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    redirect(url_for('index'))


