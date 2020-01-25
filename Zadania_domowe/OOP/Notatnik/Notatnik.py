

class Osoba:
    def __init__(self, imie, email):
        self.imie = imie
        self.email = email
        self.validate()

    def validate(self):
        if not "@" in self.email:
            raise ValueError("invalid email")


    def show(self):
        print(f"{self.imie}, email: {self.email}")

class Adres:
    def __init__(self, ulica, miasto):
        self.ulica = ulica
        self.miasto = miasto

    def show(self):
        print(f"Adres: {self.ulica}, {self.miasto}")


os = Osoba("Jacenty", "jaca92@gmail.com")
ad = Adres("Brodeckich 11", "Baboszewo")


class Kontakt(Osoba, Adres):
    def __init__(self, os: Osoba, ad: Adres):
        self.os = os
        self.ad = ad

    def show(self):
        os.show()
        ad.show()

kon = Kontakt(os, ad)
kon.show()

class Notebook(Kontakt):
    lista = {}
    def __init__(self):
        pass

    def add(self, imie, email, ulica, miasto):
        self.lista[imie] = [email, ulica, miasto]

    def show(self, imie):
        if self.lista.get(imie) == None:
            print(f"Brak wpisy dla osoby: {imie}")
        else:
            l = self.lista.get(imie)
            print(f"{imie}, email: {l[0]}\nadres: {l[1]}, {l[2]}")


note = Notebook()
note.add("Marcin", "mardzien@op.pl", "Brodeckich 11", "Baboszewo")
note.add("Krzysztof", "krzykow@gmail.com", "ul. Przedwojewo 1", "Przedwojewo")
note.show("Marcin")
note.show("Krzysztof")
note.show("Paweł")


def test_notebook_show():
    note = Notebook()
    note.add("Krzysztof", "krzykow@gmail.com", "ul. Przedwojewo 1", "Przedwojewo")
    expected = """Krzysztof, email: krzykow@gmail.com
adres: ul. Przedwojewo 1, Przedwojewo"""
    assert note.show("Krzysztof") == expected