from cashmachine import CashMachine


def test_cash_machine_initialization():
    cash_machine = CashMachine()
    assert cash_machine


def test_cash_machine_is_avaiable_when_cashmachine_is_empty():
    cash_machine = CashMachine()
    assert cash_machine.is_available is False


def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.__bills == [200, 100, 100, 50]
    assert cash_machine.is_available is True
    cash_machine.put_money([200, 100])
    assert cash_machine.__bills == [200, 100, 100, 50, 200, 100]


def test_withdraw_money_for_empty_cache_machine():
    cash_machine = CashMachine()
    assert cash_machine.withdraw_money(100) == []


def test_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([100])
    assert cash_machine.withdraw_money(100) == [100]
    assert cash_machine.is_available is False
    cash_machine.put_money([50, 50, 50])
    assert cash_machine.withdraw_money(100) == [50, 50]
    assert cash_machine.is_available is True


def test_withdraw_money_2():
    cash_machine = CashMachine()
    cash_machine.put_money([100, 50, 200])
    # [50,50,50,100,100]
    assert cash_machine.__bills == [100, 50, 200]
    assert cash_machine.withdraw_money(200) == [200]
    assert cash_machine.__bills == [100, 50]


def test_withdraw_money_3():
    cash_machine = CashMachine()
    cash_machine.put_money([50, 50, 50])
    assert cash_machine.withdraw_money(200) == []
    assert cash_machine.__bills == [50, 50, 50]
