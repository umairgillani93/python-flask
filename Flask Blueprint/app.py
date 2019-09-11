# app.py file at the same level myproject directory!

from myproject import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)
