"""
Terminologia:

Obiekt, Typ, instancja, atrybut, metoda

słowo kluczowe class a po nim Nazwa klasy

"""

class Osoba:
    gatunek = "Homo Sapiens"  # atrybut klasowy

    def __init__(self, imie, wiek, wzrost):  # metoda specjalna
        self.imie = imie  # atrybt intancji
        self.wiek = wiek
        self.wzrost = wzrost
        self.rok_ur = 2019 - wiek
        self.energia = 500

    def idz(self):
        print(f"{self.imie} idzie")
        self.energia -= 40

    def spij(self):
        print(f"{self.imie} śpi")
        self.energia += 30

if __name__ == "__main__":
    print(__name__)
    
    os1 = Osoba("Rafał", 40, 181)
    os1.idz()
    print(os1.energia)
    os1.spij()
    print(os1.energia)

    os2 = Osoba("Adam", 34, 182)
    print(os1.gatunek)
    print(os2.gatunek)
    Osoba.gatunek = "Homo Australopitekus"
    print(os1.gatunek)
    # os1.imie = "Rafał"
    # os1.wiek = 40

    print(os1.imie)
    print(os1.wzrost)
    print(os1.rok_ur)