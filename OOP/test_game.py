
from game import Postac, Przedmiot

class TestPostac:
    def test_postac_initialization(self):
        hero = Postac("Hi-men", 1000, 100)
        assert hero
        assert hero.imie =="Hi-men"
        assert hero.zycie == 1000
        assert hero.sila == 100

    def test_postac_wez_przedmiot(self):
        hero = Postac("Hi-men", 1000, 100)
        siekiera = Przedmiot("Krwawa siekiera", 50, 5, 4)
        hero.wez_przedmiot(siekiera)
        noz = Przedmiot("Ostrze prawdy", 25, 5, 2)
        hero.wez_przedmiot(noz)
        assert hero.atak == 100 + 50 + 25

    def test_obrazenia(self):
        hero = Postac("Hi-men", 1000, 100)
        hero.obrazenia(200)
        assert hero.zycie == 800

    def test_zyje(self):
        hero = Postac("Hi-men", 1000, 100)
        assert hero.zyje is True
        hero.obrazenia(1000)
        assert hero.zyje is False


class TestPrzedmiot:
    def test_przedmiot_initialization(self):
        siekiera = Przedmiot("Krwawa siekiera", 50, 5, 4)
        assert siekiera
        assert siekiera.nazwa == "Krwawa siekiera"
        assert siekiera.bonus_ataku == 50
        assert siekiera.bonus_obrony == 5
        assert siekiera.miejsce == 4

