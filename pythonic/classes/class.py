
class Spam:
    def eggs(self):
        pass
    def _beverage(self):
        pass

s = Spam()
s.eggs
s.toast = 'buttered'
print(s.toast)
s._beverage()


class Rabbit:

    def __init__(self, size, danger):
        self._size = size
        self._danger = danger
        self._victims = []
    
    def threaten(self):
        print("I am a {} bunny with {}!".format(self._size, self._danger))

r1 = Rabbit('large', 'sharp pointy teeth')
r1.threaten()

r2 = Rabbit('small', 'fluffy and furry')
r2.threaten()


class Knight:
    def __init__(self, name):
        self._name = name
    
    # getter method
    def get_name(self):
        return self._name
    
    # setter method
    def set_name(self, name):
        self._name = name

k = Knight("Lancelot")
print(k.get_name())

# @property decorator to a method with the name you want. It receives no parameters other than self.