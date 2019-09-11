import os
from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

api = Api(app)
jwt = JWT(app, authenticate, identity)

#######################################
######### MODELS ######################
######################################

class Kitten(db.Model):

    name = db.Column(db.String(80), primary_key = True)

    def __init__(self):
        self.name = name

    def json(self):
        return {'name': self.name} # API send and receive data in the form of Json object!

class KittenNames(Resource):

    def get(self, name):

        kit = Kitten.query.filter_by(name = name).first()
        if kit:
            return kit.json()
        else:
            return {'name':None}, 404

    def post(self, name):

        kit = Kitten(name=name)
        db.session.add(kit)
        db.commit()

        return kit.json()

    def delete(self, name):

        kit = Kitten.query.filter_by(name = name).first()
        db.session.delete(kit)
        db.session.commit()

        return {'Note': 'delete success'}

class AllNames(Resource):

    # @jwt_required()
    def get(self):
        kittens = Kitten.query.all()

        return [kit.json() for kit in kittens]

api.add_resource(KittenNames, '/kitten/<string:name>')
api.add_resource(AllNames, '/kittens')

if __name__ == '__main__':
    app.run(debug = True)
