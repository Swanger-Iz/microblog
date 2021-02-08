from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    # posts
    # Переменная для высокоуровневой связи таблиц User -> Posts
    # здесь отношение один ко многим (один пользователь может написать много сообщений)
    # backref - определяет имя поля, которое будет добавлено к объектам класса «много», 
    # который указывает на объект «один». то добавит выражение post.author, которое
    # вернет автора сообщения. Аргумент lazy определяет, как будет выполняться запрос базы данных для связи
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return 'User {}'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)