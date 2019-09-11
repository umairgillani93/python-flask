from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def newindex():
    return render_template('newindex.html')

@app.route('/newsignup')
def newsignup():
    return render_template('newsignup.html')

@app.route('/newthankyou')
def newthankyou():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('newthankyou.html', first = first, last = last)

@app.route('/newwelcome')
def welcome():
    return render_template('newwelcom.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.errorhandler(404)
def new404(e):
    return render_template('new404.html'), 404

if __name__ == '__main__':
    app.run(debug = True)
