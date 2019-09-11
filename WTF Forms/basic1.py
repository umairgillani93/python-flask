from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import FlaskForm # to create our own forms with Flask
from wtforms import StringField, SubmitField # essential fields to sumbit the form

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey' # configure a key, for CSRF security work from configuration dictionary

# now we wanna create a WTF form class, and then we wanna set up a view function
# that creates the instance of that form class, and then checks if it's a valid submission

class InfoForm(FlaskForm): # form class

    breed = StringField('What Breed are you?') # for string field just put string as a label
    submit = SubmitField('Submit')

    # The attributes could be sent back to the html templates

# now let's set up our view function
@app.route('/', methods = ['GET', 'POST']) # set the methods, for passing in the forms to the template
def index():

    breed = False
    form = InfoForm()

    if form.validate_on_submit():

        breed = form.breed.data # if the form submission is valid, pass in the form data to breed object
        form.breed.data = ''

    return render_template('index1.html', form = form, breed = breed)

if __name__ == '__main__':
    app.run(debug = True)
