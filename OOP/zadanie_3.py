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

def test_electric_car_initialization():
    car = ElectricCar(100)
    assert car.max_range == 100

def test_electric_car_drive():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30

def test_electric_car_drive_over_max_range_in_one_travel():
    car = ElectricCar(100)
    assert car.drive(120) == 100

def test_electric_car_charge():
    car = ElectricCar(100)
    assert car.drive(100) == 100
    assert car.drive(30) == 0
    assert car.max_range == 100
    assert car.traveled_distance == 100
    car.charge()
    assert car.max_range == 100
    assert car.drive(30) == 30
    assert car.traveled_distance == 30

def test_electric_car_cannot_overload():
    car = ElectricCar(100)
    assert car.drive(10) == 10
    car.charge()
    assert car.max_range == 100
    assert car.traveled_distance == 0