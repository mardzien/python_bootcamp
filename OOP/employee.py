class Employee:

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.do_wyplaty = 0

    def register_time(self, czas):

        self.czas = czas
        if czas <= 8:
            self.do_wyplaty = czas * self.stawka
        if czas > 8:
            self.do_wyplaty = 8 * self.stawka + 2 * (czas - 8) * self.stawka
        return self.do_wyplaty

    def pay_salary(self):
        print(f"{self.do_wyplaty}")
        self.do_wyplaty = 0

class PremiumEmployee(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.bonus = 0

    def give_bonus(self, value):
        self.bonus += value

    def pay_salary(self):
        

pracownik = Employee("Jan", "Kowalski", 100.0)
pracownik.register_time(5)
pracownik.pay_salary()
pracownik.pay_salary()
pracownik.register_time(10)
pracownik.pay_salary()

superpracownik = PremiumEmployee("Janek", "Kowal", 100.0)
superpracownik.register_time(8)
superpracownik.give_bonus(1000.0)
superpracownik.pay_salary()