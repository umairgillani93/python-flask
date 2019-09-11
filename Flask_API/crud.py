from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

api = Api(app)
jwt = JWT(app, authenticate, identity)

kittens = []

class KittenNames(Resource):

    def get(self, name):
        for kit in kittens:
            if kit['name'] == name:
                return kit
        return {'name':None}

    def post(self, name):
        kit = {'name':name}
        kittens.append(kit)
        return kit

    def delete(self, name):
        for ind,kit in enumerate(kittens):
            if kit['name'] == name:
                deleted_kit = kitten.pop(ind)

            return {'Note': 'delete success'}

class AllNames(Resource):

    @jwt_required()
    def get(self):
        return {'kittens': kittens}

api.add_resource(KittenNames, '/kitten/<string:name>')
api.add_resource(AllNames, '/kittens')

if __name__ == '__main__':
    app.run(debug = True)
