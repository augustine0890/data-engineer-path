
class Speical:
    def __init__(self, value):
        self._value = value
    
    def __add__(self, other):
        return self._value + other._value
    
    def __str__(self):
        return self._value.upper()
    
    def __eq__(self, other):
        return self._value == other._value

if __name__ == '__main__':
    s = Speical("spam")
    e = Speical("eggs")
    u = Speical("spam")
    n = Speical(5)
    o = Speical(15)

    print("s + s", s + s)
    print("s + t", s + e)

    print("s == s", s == s)
    print("s == e", e == s)

    print("n + o", n + o)
    print("n == n", n == n)
    print("n == o", n == o)

    print("str(s)={} str(e)={}".format(str(s), str(e)))
    print("id(s)={} id(u)={}".format(id(s), id(u)))

