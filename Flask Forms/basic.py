from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('thankyou.html', first = first, last = last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/overview')
def overview():
    return render_template('overview.html')


if __name__ == '__main__':
    app.run(debug = True)
