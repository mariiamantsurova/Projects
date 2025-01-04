class Sqrt:
    def __init__(self, func):
        self._func = func
    def __call__(self, a, b):
        result = self._func(a, b)
        if result < 0:
            return -1
        return result ** 0.5

@Sqrt
def add_values(n1, n2):
    return n1 + n2

@Sqrt
def substract_values(n1, n2):
    return n1 - n2


print(add_values(10, 20))
print(add_values(10, -20))
print(substract_values(100, 19))
print(substract_values(10, 19))