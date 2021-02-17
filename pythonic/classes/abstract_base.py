from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("woof woof!")

class Cat(Animal):
    def speak(self):
        print("Meow meow meow")

class Duck(Animal):
    pass


d = Dog()
d.speak()

c = Cat()
c.speak()

try:
    d = Duck()
    d.speak()
except TypeError as err:
    print(err)