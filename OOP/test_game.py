from game import Postac, Przedmiot


class TestPostac:
    def test_postac_initialization(self):
        hero = Postac("Hi-men", 100, 200)
        assert hero
        assert hero.imie == "Hi-men"
        assert hero.zycie == 100
        assert hero.sila == 200
        assert 0 <= hero.atak <= 200

    def test_postac_wez_przedmiot(self):
        hero = Postac("Hi-men", 100, 200)
        siekiera = Przedmiot("Krwawa Siekiera", 50, 5, 4)
        hero.wez_przedmiot(siekiera)
        assert hero.atak == 200 + 50
        noz = Przedmiot("Ostrze prawdy", 25, 5, 2)
        hero.wez_przedmiot(noz)
        assert hero.atak == 275

    def test_obrazenia(self):
        hero = Postac("Hi-men", 100, 200)
        hero.obrazenia(20)
        assert hero.zycie == 80

    def test_zyje(self):
        hero = Postac("Hi-men", 100, 200)
        assert hero.zyje is True
        hero.obrazenia(100)
        assert hero.zyje is False


class TestPrzedmiot:
    def test_przedmiot_initialization(self):
        siekiera = Przedmiot("Krwawa Siekiera", 50, 5, 4)
        assert siekiera
        assert siekiera.nazwa == "Krwawa Siekiera"
        assert siekiera.bonus_do_ataku == 50
        assert siekiera.bonus_do_obrony == 5
        assert siekiera.miejsce == 4
