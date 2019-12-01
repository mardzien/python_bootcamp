import pytest


class Osoba:

    def __init__(self, imie, email):
        self.imie = imie
        self.email = email
        self.validate()

    def validate(self):
        if not "@" in self.email:
            raise ValueError("Invalide user email")

    def show(self):
        return f"{self.imie}, email: {self.email}"


class Adres:

    def __init__(self, ulica, miasto):
        self.ulica = ulica
        self.miasto = miasto

    def show(self):
        return f"adres: {self.ulica}, {self.miasto}"


class Kontakt(Osoba, Adres):

    def __init__(self, imie, email, ulica, miasto):
        Osoba.__init__(self, imie, email)
        Adres.__init__(self, ulica, miasto)

    def show(self):
        return f"""{self.imie}, email: {self.email}, ulica: {self.ulica}, miasto: {self.miasto}"""


class Notebook:

    def __init__(self):
        self.kontakty = {}

    def add(self, imie, email, ulica, miasto):
        kontakt = Kontakt(imie, email, ulica, miasto)
        self.kontakty[imie] = kontakt

    def show(self, imie):
        if imie in self.kontakty:
            return self.kontakty[imie].show()
        return f"Brak wpisu dla osoby: {imie}"


def test_osoba():
    with pytest.raises(ValueError):
        os = Osoba("Zenek", "Martyniuk")

    os = Osoba("Zenek", "zenek@martyniuk.pl")
    assert os.show() == "Zenek, email: zenek@martyniuk.pl"


def test_adres():
    ad = Adres("Rynek 7", "Bielsk Podlaski")
    assert ad.show() == "adres: Rynek 7, Bielsk Podlaski"


def test_contact():
    # os = Osoba("Zenek", "zenek@martyniuk.pl")
    # ad = Adres("Rynek 7", "Bielsk Podlaski")
    contact = Kontakt("Zenek", "zenek@martyniuk.pl", "Rynek 7", "Bielsk Podlaski")
    assert contact.show() == """Zenek, email: zenek@martyniuk.pl, ulica: Rynek 7, miasto: Bielsk Podlaski"""

    # os2 = Osoba("Ania", "ania@martyniuk.pl")
    # ad2 = Adres("Rynek 9", "Gdańsk")
    contact = Kontakt("Ania", "ania@martyniuk.pl", "Rynek 9", "Gdańsk")
    assert contact.show() == """Ania, email: ania@martyniuk.pl, ulica: Rynek 9, miasto: Gdańsk"""


def test_notebook():
    notes = Notebook()
    notes.add('Ala', 'ala@wp.pl', 'Dziwna 15', 'Pacanów')
    notes.add('Robert', 'robert@gmail.com', 'Królewska 27', 'Warszawa')
    assert notes.show('Ala') == """Ala, email: ala@wp.pl, ulica: Dziwna 15, miasto: Pacanów"""
    assert notes.show('Robert') == """Robert, email: robert@gmail.com, ulica: Królewska 27, miasto: Warszawa"""
    assert notes.show("Krzyś") == "Brak wpisu dla osoby: Krzyś"
