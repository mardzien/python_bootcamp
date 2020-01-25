
class Osoba:

    def __init__(self, imie):
        self.imie = imie

class SuperSmart:

    def __init__(self):
        self.smart = True

    def calculate(self):
        print("Super calculations done!")

class SuperStrength:
    def __init__(self):
        self.super_strength = True

    def lift(self):
        print("Heavy lifting done!")

class Hero(Osoba, SuperSmart, SuperStrength):

    def __init__(self, imie):
        super().__init__(imie)

h = Hero("Rafał")
h.calculate()
h.lift()