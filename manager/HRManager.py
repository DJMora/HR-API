from containers.HRList import HRList
#Application manager

class HRManager:
    def __init__(self):
        self.employees = HRList()


    def addEmployee(self, employee):
        self.employees.addEmployee(employee)


    def deleteEmployee(self, position):
        self.employees.deleteEmployee(position)


    def updateEmployee(self, employee):
        self.employees.update(employee)


    def searchEmployee(self, name):
        return self.employees.searchEmployee(name)


    def getAllEmployees(self):
        return self.employees.getAllEmployees()
