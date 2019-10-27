


class Product:

    def __init__(self, id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"Produkt \"{self.nazwa}\", id: {self.id}, cena: {self.cena} PLN")


prod1 = Product(1, "Woda", 10.99)
prod1.print_info()