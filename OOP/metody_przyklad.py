import math

class Osoba:

    def __init__(self, name):
        self.name = name

class Grupa:

    def __init__(self):
        self.osoby = []

    def add_osoba(self, osoba):
        self.osoby.append(osoba)

    @staticmethod
    def utworz_z_osobami(osoby):
        gr = Grupa()
        for osoba in osoby:
            gr.add_osoba(osoba)
        return gr


#osoby = [Osoba("Rafał"), Osoba("Ania"), Osoba("Adam")]
#gr = Grupa.utworz_z_osobami(osoby)
#print(gr.osoby)


class Pizza:
    def __init__(self, skladniki, promien):
        self.skladniki = skladniki
        self.promien = promien

    def area(self):
        return self.circle_area(self.promien)

    @classmethod
    def prosciutto(cls):
        return cls(["szynka, mozarella, pomidory"], 30)

    @classmethod
    def margerita(cls):
        return cls(["mozarella, pomidory"], 30)


    @staticmethod
    def circle_area(r):
        return math.pi * r ** 2

    def __str__(self):
        return f"Pizza {self. promien}, {self.skladniki}"


pizza = Pizza([], 3)
print(pizza.area())

margerita = Pizza.margerita()
print(margerita)