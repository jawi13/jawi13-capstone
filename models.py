import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy

database_name = "capstone"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

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