# 4. FLASK MIGRATE
# keeps flask app connected to SQLite database using Flask-Migrate

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Once the Model is created we can no longer add columns into that, but with Migrate we can add!
Migrate(app,db) # Connects the Flask Application with the Database

############################
# 1. export FLASK_APP = flaskMigrate.py -> for LINUX
# 2. flask db init -> initilize the migrations directory
# 3. flask db migrate -m 'message' -> creates a migration file, yet to execute
# 4. flask db upgrade -> upgrades the database

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
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):  # id column will be automatically created for us
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f'Puppy {self.name} is {self.age} years old'

if __name__ == '__main__':
    app.run(debug = True)
