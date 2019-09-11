# MODEL RELATIONS
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sqlit.data')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Children(db.Model):
    __tablename__ = 'children'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    # ONE TO MANY
    # Children to many Toys..
    # 'lazy' argument below shows how the related items to be loaded
    toy = db.relationship('Toy', backref = 'children', lazy = 'dynamic')
    # ONE TO ONE
    # One Children to One Parent
    # uselist = False below for ONE TO ONE relationship
    parent = db.relationship('Parent', backref = 'children', uselist = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Children name is {self.name} and parent name is {self.parent.name}'
        else:
            return f'{self.name} has no parent registered'

    def report_toys(self):
        print("Here are my Toys")
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.Text)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'))

    def __init__(self, item_name, child_id):
        self.item_name = item_name
        self.child_id = child_id

class Parent(db.Model):
    __tablename__ = 'parent'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    child_id = db.Column(db.Integer, db.ForeignKey('children.id'))

    def __init__(self, name, child_id):
        self.name = name
        self.child_id = child_id
