class Student:
    University_Name = "BRAC University"

    """
    # default constructor
    
    def __init__(self):
        pass
    """

    # parameterized constructor

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")

# creating method

    def welcome(self):
        print("Welcome dear students")


s1 = Student("Sarwar",96) 

s1.welcome()

print(s1.name, s1.marks)

s2 = Student("Sajan",88)        
print(s2.name, s2.marks)    

print(Student.University_Name)