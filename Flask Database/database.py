# 1. FLASK DATABASE
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__)) # grabs the file to create database in
# __file__ -> home/umair/Desktop/Flask/Database/database.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICAIONS'] = False # auto 'TRACK_MODIFICATIONS' -> OFF

db = SQLAlchemy(app) # creates the database

#############################
class Puppy(db.Model):

    # Manually creating model i.e -> Tables
    __tablename__ = 'puppies'

    # now lets create different 'Columns' in our Model / Table
    # SYNTAX:
    # columName = db.Column(db.columnType, primary_key = True / False)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):  # id column will be automatically created for us
        self.name = name
        self.age = age


    def __repr__(self):
        return f'Puppy {self.name} is {self.age} years old'
