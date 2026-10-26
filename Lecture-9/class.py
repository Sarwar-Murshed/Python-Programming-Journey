class Person:
    name = "Anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Sarwar Murshed")
print(p1.name)
print(Person.name)


"""
class method(cls)
instance method(self)
static method()

"""
