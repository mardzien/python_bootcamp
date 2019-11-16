
from basket import Basket, Product


def test_basket_initialization():
    basket = Basket()
    assert basket


def test_product_initialization():
    product = Product(1, 'Woda', 10.0)
    assert product.id == 1
    assert product.name == "Woda"
    assert product.price == 10.0


def test_add_product_to_basket():
    product = Product(1, 'Woda', 10.0)
    basket = Basket()
    basket.add_product(product, 5)

def test_basket_count_total_price():
    product = Product(1, 'Woda', 10.0)
    basket = Basket()
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50
    product = Product(2, 'Piwo', 5)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50 + 25

def test_basket_generate_report():
    product = Product(1, 'Woda', 10.0)
    basket = Basket()
    basket.add_product(product, 5)
    expected = """Produkty w koszyku
- Woda (1), cena: 10.0 x 5
W sumie: 50.0
"""
    assert basket.generate_report() == expected


def test_basket_add_discount():
    product = Product(1, 'Woda', 10.0)
    basket = Basket()
    basket.add_discount(10)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50 - 10
    product = Product(2, 'Piwo', 5)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50 + 25 - 10