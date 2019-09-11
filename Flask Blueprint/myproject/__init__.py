# __init__.py file. Contains all the db and app components of the code!
# so let's quickly create some major components of the application
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)

# lets quickly register our blueprints we created previously
# In order them to work fine, we need to register them underneath the 'db' initialization

from myproject.kittens.views import kittens_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint, url_prefix = '/owners')
app.register_blueprint(kittens_blueprint, url_prefix = '/kittens')
