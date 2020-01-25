

class Circle:

    def __init__(self, r=1):
        self.radius = r

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

circle = Circle(10)
print(circle.radius)
print(circle.diameter)

circle.radius = 5
print(circle.radius)
print(circle.diameter)

circle.diameter = 20
print(circle.radius)
print(circle.diameter)
