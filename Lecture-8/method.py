class Student:

    University = "UIU"

    def __init__(self , name , marks , grade):
        self.name  = name
        self.marks = marks
        self.grade = grade


    def welcome(self):
        print("Welcome",self.name)
        print("Here is your result - ")

    def Result(self):
        print("Marks:", self.marks, "| Grade:", self.grade)
        print()

print("Student of", Student.University)    


s1 = Student("Fatima Rahman","82","B+")
s1.welcome()
s1.Result()

s2 = Student("Neha Karim","89","A-")
s2.welcome()
s2.Result()