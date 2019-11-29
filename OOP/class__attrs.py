
class Osoba:
    gatunek = "Homo Sapiens"
    NEXT_ID = 1

    def __init__(self, name):
        self.name = name
        self.id = Osoba.NEXT_ID
        Osoba.NEXT_ID += 1

os1 = Osoba("Adam")
os2 = Osoba("Ewa")

print(os1.gatunek)
print(os2.gatunek)

Osoba.gatunek = "Homo Australopitecus"

print(os1.gatunek)
print(os2.gatunek)

os2.gatunek = "Homo Sapiens"

print(os1.gatunek)
print(os2.gatunek)

print(os1.id)
print(os2.id)
print(Osoba.NEXT_ID)