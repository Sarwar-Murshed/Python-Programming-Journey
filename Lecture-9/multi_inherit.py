class Person:

    @staticmethod
    def welcome():
        print("Welcome to UIU!")

class Student:

    @staticmethod
    def study():
        print("Student is studying...")

class CSE_Student(Person, Student):

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student Name:", self.name)


s1 = CSE_Student("Sarwar")

s1.show()
s1.welcome()
s1.study()