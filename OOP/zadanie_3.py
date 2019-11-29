class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.traveled_distance = 0

    def drive(self, distance):
        if distance + self.traveled_distance > self.max_range:
            distance = self.max_range - self.traveled_distance
            self.traveled_distance = self.max_range
        else:
            self.traveled_distance += distance
        return distance

    def charge(self):
        self.traveled_distance = 0
