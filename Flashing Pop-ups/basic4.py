from flask import Flask
from flask import render_tempalte
from flask import session
from flask_wtf import FlaskForm
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):
    submit = SubmitField('Click Me')

@app.route('/', methods = ['GET','POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash('You just clicked the button!') # flashes this message back to the user!

        return redirect(url_for('index'))

    # view function returns the code below
    return render_template('index.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)
