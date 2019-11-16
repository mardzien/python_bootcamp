


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

pracownik = Employee("Jan", "Kowalski", 100.0)
pracownik.register_time(5)
pracownik.pay_salary()
pracownik.pay_salary()
pracownik.register_time(10)
pracownik.pay_salary()

def test_employee_init():
    pracownik = Employee("Pan", "XYZ", 200.0)
    assert pracownik.imie == "Pan"
    assert pracownik.nazwisko == "XYZ"
    assert pracownik.stawka == 200.0

def test_registred_time():
    pracownik = Employee("Pan", "XYZ", 200.0)
    pracownik.register_time(5)
    assert pracownik.register_time() == 5

def test_pay_salary():
    pracownik = Employee("Pan", "XYZ", 200.0)
    assert pracownik.pay_salary() == 0
    pracownik.register_time(5)
    assert pracownik.pay_salary() == 5*100
    assert pracownik.pay_salary() == 0
    pracownik.register_time(10)
    assert pracownik.pay_salary() == 8 * 100 + 2 * 2 * 100
    assert pracownik.pay_salary() == 0