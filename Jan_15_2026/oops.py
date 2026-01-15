class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def add(self, a, b):
        return a + b
    
    # class method
    @classmethod
    def changePerson(cls, type):
        cls.species = type

    # static method
    @staticmethod
    def sub(a, b):
        return a - b
    
p1 = Person("Pranav", 18)
p2 = Person("Monish", 22)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p1.add(5, 10), p2.add(4, 5))
print(p1.species, p2.species)

Person.changePerson("Alien")

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p1.add(5, 10), p2.add(4, 5))
print(p1.species, p2.species)

print(Person.sub(10, 7))
print(p1.sub(7, 8))