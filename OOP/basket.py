class Product:
    NEXT_ID = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.NEXT_ID
        Product.NEXT_ID += 1

class BasketEntry:
    def __init__(self, product: Product, amount: int):
        self.product = product
        self.amount = amount

    def count_price(self):
        return self.product.price * self.amount

    def report(self):
        return f"- {self.product.name} ({self.product.id}), cena: {self.product.price} x {self.amount}\n"

class Discount:
    def __init__(self, amount):
        self.amount = amount

class ValueDiscount(Discount):  # dziedziczenie
    #ValueDiscount dziedziczy po Discount
    pass

class PercentDiscount(Discount):
    pass

class Basket:
    def __init__(self):
        self.basket_entries = []
        self.discounts = []

    def add_product(self, product: Product, amount: int) -> None:
        # : Product, : int oraz -> None to są adnotacje. S
        # są one ignorowane przez pythona, ale są pomocne programiscie
        # oraz narzędziom do sprawdzania typowania - jak np mypy
        # basket_entry = {
        #     "product": product,
        #     "amount": amount
        # }

        basket_entry = BasketEntry(product, amount)

        in_basket = False
        for be in self.basket_entries:
            # if be['product'] == product:
            #     be['amount'] += amount
            #     in_basket = True
            if be.product == product:
                be.amount += amount
                in_basket = True

        if not in_basket:
            self.basket_entries.append(basket_entry)

    def count_total_price(self):
        total_price = 0
        for be in self.basket_entries:
            # total_price += be['product'].price * be['amount']
            total_price += be.count_price()
        value_discount = sum(self.discounts)
        total_price -= value_discount
        return total_price

    #def add_discount(self, discount):
        #self.discount = discount.

    def generate_report(self):
        report = "Produkty w koszyku\n"
        for be in self.basket_entries:
            report += be.report()
        report += f"W sumie: {self.count_total_price()}\n"
        return report

    @staticmethod
    def with_products(product_list: list):
        basket = Basket()
        for p in product_list:
            basket.add_product(p, 1)
        return basket

osoby = [Osoba("Rafał"), Osoba("Ania"), Osoba("Adam")]
gr = Grupa.utworz_z_osobami(osoby)
print(gr.osoby)

product = Product('Woda', 10.0)
product2 = Product('Wóda', 40.0)

print(product.id)
print(product2.id)