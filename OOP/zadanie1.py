

class Product:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price} PLN'

    def __str__(self):
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price} PLN'

    def __repr__(self):
        return self.__str__()