#!flask/bin/python
from flask import Flask, jsonify
from flask.ext.restful import Api, Resource, reqparse
from flask.ext.cors import CORS
from entities.Employee import Employee, EmployeeJsonEncoder
from manager.HRManager import HRManager


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
parser = reqparse.RequestParser()
parser.add_argument('name',type=str)
parser.add_argument('position',type=str)


class HRListApi(Resource):
    def __init__(self):
        self.manager = HRManager()


    def get(self):
        return jsonify(employees=self.manager.getAllEmployees())


    def post(self):
        args = parser.parse_args()
        employee = Employee()
        employee.name = args['name']
        employee.position = args['position']
        msg = self.manager.addEmployee(employee)
        return {'response': msg}


class HRApi(Resource):
    def __init__(self):
        self.manager = HRManager()


    def get(self, id):
        return jsonify(employee=self.manager.searchEmployee(id))


    def put(self, id):
        args = parser.parse_args()
        employee = self.manager.searchEmployee(id)
        employee.name = args['name']
        employee.position = args['position']
        msg = self.manager.updateEmployee(id, employee)
        return {'response': msg}


    def delete(self, id):
        msg = self.manager.deleteEmployee(id)
        return {'response': msg}


api.add_resource(HRApi, '/hr/<id>', endpoint = 'employee')
api.add_resource(HRListApi, '/hr', endpoint = 'employees')
app.json_encoder = EmployeeJsonEncoder

if __name__ == '__main__':
    app.run(debug=True)
