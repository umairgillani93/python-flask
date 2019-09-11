# models.py
from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# load_user() -> to show users pages specific to their login ID
# just like any social media website, Facebook etc.

@login_manager.user_loader
def user_load(user_id):
    return User.query.all(user_id)


class User(db.Model, UserMixin):
"""UserMixin has all the features for user logging in and authorization
that's why its' been inherited here"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True, index = True) # 64 characters long string, and unique!
    username = db.Column(db.String(64), unique = True, index = True)

    # now let's save the hashed version of the password
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password) # generate the password has from the
        # password that is provided by the user

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
