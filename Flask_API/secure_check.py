# secure_check.py

from user import User

users = [User(1, 'Umair', 'secretpassword'), User(2, 'Faizan', 'secretpass')]

# now lets map these users to their usernames

# Documentation example
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

# now lets authenticate our users
def authenticate(username, password):
    # Remember! The person using API is going to provide their username and password!
    # check if user exists
    # if yes, return user

    # tries to grab username from the dictionary we created above, if doesn't find returns None
    user = username_table.get(username, None)
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
