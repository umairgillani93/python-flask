# ADOPTION_SITE.PY
import os
from flask import Flask
from flask import render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm, AddOwnerForm

# Set the Flask application
app = Flask(__name__)

# Set the configuration keys
app.config['SECRET_KEY'] = 'mykey'

######################################
######## SQL DATABASE SECTION ########
######################################

# Setting up Database configurations
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEYMY_TRACK_MODIFICATIONS'] = False

# Creates the Database and initiate migration capability
db = SQLAlchemy(app)
migrate = Migrate(app,db)

############################
####### MODELS #############
############################

class Kitten(db.Model):

    __tablename__ = 'kittens2'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref = 'Kitten', uselist = False)

    def __init__(self, name):
        self.name  = name

    def __repr__(self):
        if self.owner:
            return f"Kitten name {self.name} has owner {self.owner.name}"
        else:
            return f"Kitten name {self.name} has no owner assigned yet!"

class Owner(db.Model):

    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    kitten_id = db.Column(db.Integer, db.ForeignKey('kittens2.id'))

    def __init__(self, name, kitten_id):
        self.name = name
        self.kitten_id = kitten_id

    def __repr__(self):
        return f"Owner Name: {self.name}"

########################################################
##### VIEWS FUNCTIONS --> HAVE FORMS IN IT #############
########################################################

# For home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/owner', methods = ['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        kit_id = form.kit_id.data

        new_owner = Owner(name, kit_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_kit'))

    return render_template('add_owner.html', form = form)


@app.route('/add', methods = ['GET', 'POST'])
def add_kit():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_kit = Kitten(name) # grabs the name of the user form User model
        db.session.add(new_kit)
        db.session.commit()

        return redirect(url_for('list_kit'))

    return render_template('add.html', form = form)

@app.route('/list')
def list_kit():

    kittens = Kitten.query.all()

    return render_template('list.html', kittens = kittens)

@app.route('/delete', methods = ['GET', 'POST'])
def del_kit():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        kitten = Kitten.query.get(id)
        db.session.delete(kitten)
        db.session.commit()

        return redirect(url_for('list_kit'))

    return render_template('delete.html', form = form)

##############################
####### RUNNING SERVER #######
##############################

if __name__ == '__main__':
    app.run(debug = True)
