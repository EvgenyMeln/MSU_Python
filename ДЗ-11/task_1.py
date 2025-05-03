class Incapsulator:
    def __init__(self, value = 0):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

a = Incapsulator()
print(a.get_value())

a.set_value(5.0)
print(a.get_value())

a.set_value(-1.0)
print(a.get_value())
