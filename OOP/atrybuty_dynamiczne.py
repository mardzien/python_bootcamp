

class Osoba:
    def __init__(self, imie, rok_ur):

        self.imie = imie
        self.rok_ur = rok_ur
    @property
    def wiek(self):
        return 2019 - self.rok_ur

os1 = Osoba("Paweł", 1992)
print(os1.wiek)