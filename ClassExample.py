class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"
    # Class Variable
    animal = 'dog'
    #Constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color
        # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
# Driver code
# Object instantiation

class Person:
    # init method or constructor
    def __init__(self, name):
        self.name = name
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person('Dharma')
#Hello, my name is Dharma
p.say_hi()

Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
# Accessing class attributes
print(Rodger.attr1)
# and method through objects
Rodger.fun()
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)


