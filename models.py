import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def setup_db(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)

class Actor(db.Model):
    __tablename__ = 'actor'
    id = Column(Integer(), primary_key=True)
    name = Column(String)
    age = Column(Integer())
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

class Movie(db.Model):
    __tablename__ = 'movie'
    id = Column(Integer(), primary_key=True)
    title = Column(String)
    release_year = Column(Integer)

    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
        }