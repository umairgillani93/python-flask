from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thesecretkey'

class FormInfo(FlaskForm):
    name = StringField('Enter your name here: ')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    name = True
    form = FormInfo()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index2.html', name = name, form = form)

if __name__ == '__main__':
    app.run(debug = True)
