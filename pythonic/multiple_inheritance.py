
class AnimalBase:
    def __init__(self, name):
        self._name = name
    
    def get_id(self):
        print(self._name)


class CanBark:
    def bark(self):
        print("woof-woof")


class CanFly:
    def fly(self):
        print("I'm flying")


class Dog(CanBark, AnimalBase):
    pass


class Sparrow(CanFly, AnimalBase):
    pass


d = Dog("Dennis")
d.get_id()
d.bark()

s = Sparrow("Steve")
s.get_id()
s.fly()

print(Sparrow.mro())
