# myproject/owners/views.py
from flask import Blueprint, render_template, redirect, url_for
from myproject import db # reference to the database in __init__.py file
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint('owners', __name__, template_folder = 'templates/owners') # first thing is create a Blueprint and pass in a name!,
# built-in __name__ varialbe and then assign a template folder

@owners_blueprint.route('/add', methods = ['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        kit_id = form.kit_id.data

        new_owner = Owner(name, kit_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('kittens2.list'))

    return render_template('add_owner.html', form = form)
