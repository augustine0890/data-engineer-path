
class Knight:
    def __init__(self, name, title, color):
        self._name = name
        self._title = title
        self._color = color
    
    @property
    def name(self):
        return self._name
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if isinstance(color, str):
            self._color = color
        else:
            print("Make sure enter a valid color")
    
    @color.deleter
    def color(self):
        del self._color

    @property
    def title(self):
        return self._title

k = Knight('Tom', 'Mr', 'black')
print('{} {}'.format(k.name, k.color))
k.color = 4
print('{} {}'.format(k.name, k.color))