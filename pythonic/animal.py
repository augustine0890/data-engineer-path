
class Animal:
    count = 0

    def __init__(self, species, name, sound):
        self._species = species
        self._name = name
        self._sound = sound
        Animal.count += 1
    
    @property
    def species(self):
        return self._species
    
    @classmethod
    def kill(cls):
        cls.count -= 1
    
    @property
    def name(self):
        return self._name
    
    def make_sound(self):
        print(self._sound)
    
    @classmethod
    def remove(cls):
        cls.count -= 1
    
    # Takes cls as firs param and can access or modify class state
    @classmethod
    def zoo_size(cls):
        return cls.count

    # Don't require any of the data in the class (logic out of several methods-utility functions)
    @staticmethod
    def is_big(size):
        return size > 5

if __name__ == "__main__":
    leo = Animal("African lion", "Leo", "Roarrr..")
    garfield = Animal("Cat", "Garfield", "Meoww..")
    felix = Animal("Cat", "Felix", "Meoww..")

    print(leo.name, "is a", leo.species, "--", end=" ")
    leo.make_sound()

    print(Animal.is_big(6))