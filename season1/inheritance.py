class Person(object):
      
    # Constructor
    def __init__(self, name):
        self.name = name
  
    # To get name
    def getName(self):
        return self.name
  
    # To check if this person is an employee
    def isEmployee(self):
        return False
  
  
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
  
    # Here we return true
    def isEmployee(self):
        return True
  
# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
  
emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())