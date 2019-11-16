
class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.energia = 100
        self.sila = 50

    def idz(self):
        print(f"{self.name} idzie.")

class Kot(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.sila = 30
    def daj_glos(self):
        print("Miau")

class Pies(Animal):
    def __init__(self, *args):
        super().__init__(*args)
        self.sila = 50
    def daj_glos(self):
        print("Hau")

mruczek = Kot("Mruczek", 2, "male")
saba = Pies("Saba", 3, "female")

mruczek.daj_glos()
saba.daj_glos()

mruczek.idz()
saba.idz()