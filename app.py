# There are two ways of creating REST APIs in flask
# 1. Using flask without any external
# 2. Using flask_restful library
# we will use the 2nd  version #2

from flask import *
import pymysql  #for database connection
from flask_restful import Resource, Api
# create a flask app 
app = Flask(__name__)

#create an Api object
api = Api(app)

# we need to make a class for a particular Resource
# the class will inherit from the Resource thus implementing POST, GET, DELETE and PUT request methods

class Employees(Resource):
    def get(self):
        return jsonify({"message": "GET REQUEST"})
    
    def post(self):
        return jsonify({"message": "POST REQUEST"})
    
    def put(self):
        return jsonify({"message": "PUT REQUEST"})
    
    def delete(self):
        return jsonify({"message": "DELETE REQUEST"})
    
# we need to add our resource/class that we defined along with its corresponding url

api.add_resource(Employees,'/employees')

if __name__ == '__main__':
    app.run(debug=True)