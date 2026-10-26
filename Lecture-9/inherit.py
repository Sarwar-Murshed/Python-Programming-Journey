class Car:

    color = "Black"
    
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):   # all methods and properties of Car class will be available in this class also

    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

car1.start()
print(car1.name)
print(car1.color)