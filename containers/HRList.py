from entities.Employee import Employee
#Container class for Employees

hr = [Employee('Leonardo Chen', 'Java developer')]

class HRList:
    def __init__(self):
        self.employees = hr


    def addEmployee(self, employee=Employee()):
        self.employees.append(employee)
        return 'Employee has been added'


    def deleteEmployee(self , position='PR'):
        for employee in self.employees:
            if employee.position == position:
                name = employee.name
                self.employees.remove(employee)
                return name + ' has been deleted'


    def updateEmployee(self, name='Cindy', updatedEmployee=Employee()):
        for employee in self.employees:
            if employee.name == name:
                print(employee.name + " " + employee.position)
                employee = updatedEmployee
                print(updatedEmployee.name + " " + updatedEmployee.position)
                return 'Employee has been updated'


    def searchEmployee(self, name='Cindy'):
        for employee in self.employees:
            if employee.name == name:
                return employee


    def getAllEmployees(self):
        return self.employees
