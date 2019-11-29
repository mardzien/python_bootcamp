
class CashMachine:

    def __init__(self):
        self._bills = []

    @property
    def is_available(self):
        # if self.bills:
        #     return True
        # return False
        return bool(self.__bills)

    def put_money(self, bills):
        self.__bills.extend(bills)

    def withdraw_money(self, amount):
        to_withdraw = []
        for bill in sorted(self.__bills, reverse=True):
            if bill + sum(to_withdraw) <= amount:
                to_withdraw.append(bill)
        if sum(to_withdraw) == amount:
            for bill in to_withdraw:
                self.__bills.remove(bill)
        else:
            return []
        return to_withdraw

    def print_bills(self):
        print(self.__bills)


bankomat = CashMachine()

bankomat.put_money([100, 200, 200])
print(bankomat.is_available)
bankomat.__bills = "12312313"
print(bankomat.__bills)
bankomat.print_bills()
