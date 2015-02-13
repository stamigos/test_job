from library import db, app
import flask.ext.whooshalchemy as whooshalchemy
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1

books = db.Table('books',
                 db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                 db.Column('author_id', db.Integer, db.ForeignKey('author.id')))


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(10))
    email = db.Column('email', db.String(50), unique=True, index=True)
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.username


class Book(db.Model):
    __searchable__ = ['title']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

    def __repr__(self):
        return '<Book %r>' % self.title


class Author(db.Model):
    __searchable__ = ['name']

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', secondary=books,
                            backref=db.backref('authors', lazy='dynamic'))

    def __repr__(self):
        return '<Author %r>' % self.name


whooshalchemy.whoosh_index(app, Author)
whooshalchemy.whoosh_index(app, Book)