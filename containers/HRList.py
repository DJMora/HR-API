from entities.Employee import Employee
#Container class for Employees

class HRList:
    def __init__(self):
        self.employees = [{'Leonardo Chen': 'Java Developer'}]


    def addEmployee(self, employee=Employee()):
        self.employees.append(employee)
        return 'Employee has been added'


    def deleteEmployee(self , position='PR'):
        for employee in self.employees:
            if employee.position == position:
                self.employees.remove(employee)
                return 'Employee has been deleted'


    def updateEmployee(self, updatedEmployee=Employee()):
        for employee in self.employees:
            if employee.name == updatedEmployee.name:
                employee = updatedEmployee
                return 'Employee has been updated'


    def searchEmployee(self, name='Cindy'):
        for employee in self.employees:
            if employee.name == name:
                return employee


    def getAllEmployees(self):
        return self.employees
