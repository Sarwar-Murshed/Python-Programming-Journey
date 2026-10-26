"""
Define a Circle class to create a circle with radius r using the constructor.
- Define an Area() method of the class which calculates the area of the circle.
- Define a Perimeter() method of the class which allows you to calculate the perimeter of
  the circle. """

class Circle:
    def __init__(self, r):
        self.r = r

    def Area(self):
        print("Area of Circle:", 3.1416 * self.r ** 2)

    def Perimeter(self):
        print("Perimeter of Circle:", 2 * 3.1416 * self.r)


c1 = Circle(5)

c1.Area()
c1.Perimeter()