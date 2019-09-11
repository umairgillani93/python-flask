# __init__.py
import os
from flask import Flasks
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

basedir = os.path.abspth(os.path.dirname(__file__))
app.congif['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

login_manager.init_app()  # initiate the app. Configures the management operations!
login_manager.login_view = 'login' # redirects to the 'login' view function
