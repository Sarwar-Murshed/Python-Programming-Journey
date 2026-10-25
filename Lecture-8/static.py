
class Student:
    def __init__(self,name,marks):
        self.name  = name
        self.marks = marks
 

    @staticmethod
    def University():   # without writing self
        print("United International University\n")

    def get_avg(self):
        sum = 0

        for val in self.marks:
            sum += val  

        print("Hi",s1.name,"\nYour average score is",sum/3)   

s1 = Student("Bruce Wayne",[89,92,83])

s1.University()
s1.get_avg()