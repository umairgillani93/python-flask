from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.kittens.forms import AddForm, DelForm
from myproject.models import Kitten

# First thing is, we need to set up the blueprints
# And then in order them to work normal we need to register them in the __init__.py file

kittens_blueprint = Blueprint('kittens', __name__, template_folder = 'templates/kittens')

@kittens_blueprint.route('/add', methods = ['GET','POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_kit = Kitten(name) # grabs the name of the user form User model
        db.session.add(new_kit)
        db.session.commit()

        return redirect(url_for('kittens.list'))

    return render_template('add.html', form = form)

@kittens_blueprint.route('/list')
def list():

    kittens = Kitten.query.all()

    return render_template('list.html', kittens = kittens)

@kittens_blueprint.route('/delete', methods = ['GET','POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        kitten = Kitten.query.get(id)
        db.session.delete(kitten)
        db.session.commit()

        return redirect(url_for('kittens.list'))

    return render_template('delete.html', form = form)
