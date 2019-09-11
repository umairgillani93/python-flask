# MODELS.PY FILE
from myproject import db
# since myproject has a file name __init__.py that contains all the db and app componentsself.
# So, we need to import db somehow inside __init__.py and then the above import is gonna work!

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
