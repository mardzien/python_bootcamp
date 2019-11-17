
class Osoba:

    def __init__(self, imie, rok_ur):
        self.imie = imie
        self.rok_ur = rok_ur

    @property
    def wiek(self):
        return 2019-self.rok_ur

    @property
    def czy_pelnoletni(self):
        if self.wiek >= 18:
            return True
        return False

os1 = Osoba("Rafał", 1980)
print(os1.wiek)
print(os1.czy_pelnoletni)


os1 = Osoba("Gabi", 2012)
print(os1.wiek)
print(os1.czy_pelnoletni)

print(getattr(os1, 'wiek'))
print(os1.wiek)

if hasattr(os1, 'aaa'):