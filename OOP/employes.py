class Employee:

    def __init__(self, name, last_name, rate):
        self.name = name
        self.last_name = last_name
        self.rate = rate
        self.__registered_time = 0

    def register_time(self, time):
        self.__registered_time = time

    def pay_salary(self):
        if self.__registered_time < 8:
            to_pay = self.rate * self.__registered_time
        else:
            to_pay = 8 * self.rate + (self.__registered_time - 8) * self.rate * 2
        self.__registered_time = 0
        return to_pay


class PremiumEmployee(Employee):

    def __init__(self, *args):
        super().__init__(*args)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus += amount

    def pay_salary(self):
        to_pay = super().pay_salary()
        to_pay += self.bonus
        self.bonus = 0
        return to_pay