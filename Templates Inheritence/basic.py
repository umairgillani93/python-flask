from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/star/<star_name>')
def starName(star_name):
    return render_template('star.html', star_name = star_name)

if __name__ == '__main__':
    app.run(debug = True)
