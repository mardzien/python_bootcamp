from employee import Employee, PremiumEmployee

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

def test_give_bonus():
    pracownik = PremiumEmployee("Jan", "Kowalski", 100.0)
    assert pracownik.pay_salary() == 0
    pracownik.register_time(5)
    pracownik.give_bonus(1000.0)
    assert pracownik.pay_salary() == 1500.0

