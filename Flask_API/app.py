from flask import Flask
from flask_restful import Resource, Api # Resource -> which we want to connect with
# Api, way of connecting to the Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource): # create a resource to be connected with

    def get(self):
        return {'hello':'world'}

api.add_resource(HelloWorld, '/') # adding the resource


if __name__ == '__main__':
    app.run(debug = True)
