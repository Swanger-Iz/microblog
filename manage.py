# -*- coding: utf-8 -*-
# Учебник - https://habr.com/en/post/346306/
 
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    print('Started')
    return {'db': db, 'User': User, 'Post': Post}
