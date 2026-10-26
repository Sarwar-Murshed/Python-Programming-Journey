class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Shardha") 
print(s1.name)        # prints the name
del s1.name
print(s1.name)        # nothing left