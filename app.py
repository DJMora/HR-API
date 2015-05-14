#!flask/bin/python
from flask import Flask, jsonify
from flask.ext.restful import Api, Resource, reqparse
from entities.Employee import Employee, EmployeeJsonEncoder
from manager.HRManager import HRManager


app = Flask(__name__)
api = Api(app)
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


    def get(self, name):
        employee = self.manager.searchEmployee(name)
        return {'employee': employee}



    def put(self, name):
        args = parser.parse_args()
        employee = Employee()
        employee.name = args['name']
        employee.position = args['position']
        employee = self.manager.searchEmployee(name)
        msg = self.manager.updateEmployee(employee)
        return {'response': msg}


    def delete(self, position):
        msg = self.manager.deleteEmployee(position)
        return {'response': msg}


api.add_resource(HRApi, '/hr/<id>', endpoint = 'employee')
api.add_resource(HRListApi, '/hr', endpoint = 'employees')
app.json_encoder = EmployeeJsonEncoder

if __name__ == '__main__':
    app.run(debug=True)
