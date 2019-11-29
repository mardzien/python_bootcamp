from basket import Basket, Product, ValueDiscount, PercentDiscount


def test_basket_initialization():
    basket = Basket()
    assert basket


def test_product_initialization():
    product = Product('Woda', 10.0)
    assert product.id == 1
    assert product.name == "Woda"
    assert product.price == 10.0
    Product.NEXT_ID = 1


def test_add_product_to_basket():
    product = Product('Woda', 10.0)
    basket = Basket()
    basket.add_product(product, 5)
    Product.NEXT_ID = 1


def test_basket_count_total_price():
    product = Product('Woda', 10.0)
    basket = Basket()
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50
    product = Product('Piwo', 5)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50 + 25
    Product.NEXT_ID = 1


def test_basket_generate_report():
    product = Product('Woda', 10.0)
    basket = Basket()
    basket.add_product(product, 5)
    expected = """Produkty w koszyku
- Woda (1), cena: 10.0 x 5
W sumie: 50.0
"""
    assert basket.generate_report() == expected


def test_basket_add_discount():
    product = Product('Woda', 10.0)
    basket = Basket()
    discount = ValueDiscount(10)
    basket.add_discount(discount)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50 - 10
    product = Product('Piwo', 5)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50 + 25 - 10


def test_basket_add_percent_discount():
    product = Product('Woda', 10.0)
    basket = Basket()
    discount = PercentDiscount(10)
    basket.add_discount(discount)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 5 * 10 - (5 * 10) / 10


def test_basket_with_products():
    pr1 = Product("Woda", 1)
    pr2 = Product("Chleb", 2)
    basket = Basket.with_products([pr1, pr2])
    assert basket.count_total_price() == 3
