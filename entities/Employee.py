from flask.json import JSONEncoder
#Basic employee representation

class Employee:
    def __init__(self, name='Cindy Rojas', position='PR'):
        self.name = name
        self.position = position


#Encoder class to make Employee serializable
class EmployeeJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Employee):
            return {
                'name': obj.name,
                'position': obj.position
            }

        return super(EmployeeJsonEncoder, self).default(obj)
