class SpyingNumber:
    _global_counter = 0
    
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"SpyingNumber({self.value})"

    def __str__(self):
        return str(self.value)

    def _increment_counter(self):
        SpyingNumber._global_counter += 1

    @staticmethod
    def get_global_counter():
        return SpyingNumber._global_counter

    @staticmethod
    def reset_global_counter():
        SpyingNumber._global_counter = 0

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        if isinstance(other, SpyingNumber):
            self._increment_counter()
            return SpyingNumber(self.value + other.value)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        if isinstance(other, SpyingNumber):
            self._increment_counter()
            return SpyingNumber(self.value - other.value)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        if isinstance(other, SpyingNumber):
            self._increment_counter()
            return SpyingNumber(self.value * other.value)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        if isinstance(other, SpyingNumber):
            self._increment_counter()
            return SpyingNumber(self.value / other.value)

print(SpyingNumber.get_global_counter())

x = SpyingNumber(10)
print(x)

x = x + 10
