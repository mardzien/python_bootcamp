

class CashMachine:

    def __init__(self):
        self.bills = []

    @property
    def is_available(self):
        return bool(self.bills)

    def put_money(self, bills):
        self.bills.extend(bills)

    def withdraw_money(self, amount):
        to_withdraw = []
        for bill in sorted(self.bills, reverse = True):
            if bill + sum(to_withdraw) <= amount:
                to_withdraw.append(bill)
        if sum (to_withdraw) == amount:
            for bill in to_withdraw:
                self.bills.remove(bill)
        else:
            return []
        return to_withdraw