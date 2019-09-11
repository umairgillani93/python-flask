from flask import Flask
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField
from wtforms import RadioField, SelectField, TextField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):

    # This 'validator' argument imported from wtforms will automatically check
    # if there is any data passed in the field..
    breed = StringField('What breed are you? ', validators = [DataRequired()])

    adopted = BooleanField('Have you been adopted? ')
    mood = RadioField('Pleae choose your mood:',
                    choices = [('mood_one', 'Happy'), ('mood_two','Excited')]) # bunch of radio buttons

    food_choice = SelectField('Pick your favorite food:',
                    choices = [('chi','Chicken'), ('bf','Beef'), ('fsh','Fish')])

    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET','POST'])
def index():

    form = InfoForm()

    # In order to pass all that form data to another template automatically, we're gonna be using
    # the 'session' object we imported from flask. unlike cockies the 'session' data is stored
    # on server. And a session is time intervel when a client is logging in to the time when he
    # logs out from the server.
    # so the data stores in a temporary directory on a server

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['adopted'] = form.adopted.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou')) # redirect to 'thankyou' page only upon valid submisson

    return render_template('index3.html', form = form) # whole return of the function

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou3.html')

if __name__ == '__main__':
    app.run(debug = True)
