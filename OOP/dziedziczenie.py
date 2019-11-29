class Animal:
    def __init__(self, name, wiek, plec):
        self.name = name
        self.wiek = wiek
        self.plec = plec
        self.energia = 100

    def idz(self):
        print(f"{self.name} idzie!")

class Kot(Animal):
    def __init__(self, *args):
        super().__init__(*args)
        self.sila = 30

    def daj_glos(self):
        print("Miau")

class Pies(Animal):
    def __init__(self, *args):
        # super().__init__(name, wiek, plec)
        super(Pies, self).__init__(*args)
        self.sila = 50

    def daj_glos(self):
        print("Hau")


mruczek = Kot("Mruczek", 2, "samiec")
saba = Pies("Saba", 3, "samica")

mruczek.daj_glos()
saba.daj_glos()

mruczek.idz()
saba.idz()

print(saba.sila > mruczek.sila)