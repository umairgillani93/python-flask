from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# Routing examples
# Redirecting to a particular page
@app.route('/')
def index():
    return '<h1> This is my first website </h1>'

# Default routing
@app.route('/home', defaults = {'name': 'umair shah'})
@app.route('/<name>')
def first_name(name):
    return 'the name is: ' + name

# Web applications use different HTTP methods when accesing URLS
# By default a 'route' only answers to GET requests
# POST is used when there's need to get the data from user

@app.route('/bacon', methods = ['GET', 'POST'])
def bacon():
    if request.method == 'GET':
        return 'You are using GET method'
    else:
        return 'You are using POST method'

#def do_the_login():
    #pass

#def show_the_login_form():
    #pass

#@app.route('/login', methods = ['GET', 'POST'])
#def login():
    #if request.method == 'GET':
        #show_the_login_form()
    #else:
        #do_the_login()

# Rendering Templates
@app.route('/profile/<username>')
def users(username):
    return render_template('profile.html', username = username)


# Accessing request data

with app.test_request_context('/hello', method='POST'):

    assert request.path == '/hello'
    assert request.method == 'POST'
The other possibility is passing a whole WSGI environment to the request_context() method:

from flask import request

with app.request_context(environ):
    assert request.method == 'POST'

if __name__ == '__main__':
    app.run(debug = True)
