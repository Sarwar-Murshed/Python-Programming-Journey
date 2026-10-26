"""
Define an Employee class with attributes role, department and salary. This class also 
has a showDetails() method.
Create an Engineer class that inherits properties from Employee and has additional 
attributes:name and age

"""

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role :",self.role,"  |   Dept :",self.dept," | Salary :",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        super().__init__("Engineer","IT",75000)
        self.name = name
        self.age = age

eng1 = Engineer("Elon Musk",52)
eng1.showDetails()