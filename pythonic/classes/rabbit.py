
class Rabbit:
    LOCATION = "the Cave of Caerbannog"

    def __init__(self, weapon):
        self.weapon = weapon
    
    def display(self):
        print("This rabbit guaring {} uses {} as a weapon!".format(self.LOCATION, self.weapon))

    @classmethod
    def get_location(cls):
        return cls.LOCATION.capitalize()

print(Rabbit.get_location())
r1 = Rabbit("sword")
r1.display()
print(r1.get_location())