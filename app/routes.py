# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index/')
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
    form = LoginForm()
    # Логи
    print(form.username.data, form.password.data, form.remember_me.data)
    # form.validate_on_submit()
    # 1. Запускает все варидаторы (форму ввода пользователя, пароля и т.д.)
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data)) # flash - исп-ся для вывода сообщений и т.д.
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)




