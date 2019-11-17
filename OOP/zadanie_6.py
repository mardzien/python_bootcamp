import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        #self_len = math.sqrt(pow(self.x, 2) + pow(self.x, 2))
        #other_len = math.sqrt(pow(other.x, 2) + pow(other.x, 2))
        #return self_len > other_len
        return self.length() > other.length()

    def length(self):
        return math.sqrt(pow(self.x, 2) + pow(self.x, 2))

    def __str__(self):
        return f"Vector (x = {self.x}, y = {self.y})"