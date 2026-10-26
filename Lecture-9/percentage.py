class Student:
    def __init__(self,phy,chemi,math):
        self.phy = phy
        self.chemi = chemi
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chemi + self.math)/3) + "%"



stu1 = Student(95,95,90)
print(stu1.percentage)  

#modifying or changing marks

stu1.math = 92
print(stu1.percentage)