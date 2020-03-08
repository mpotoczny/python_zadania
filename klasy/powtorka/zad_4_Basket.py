"""
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w określonej liczbie do koszyka.
Zaimplementuj metodę obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości koszyka.
Dodanie dwa razy tego samego produktu do koszyka powinno stworzyć tylko jedną pozycję.
Przykład użycia:
basket = Basket()
product = Product(1, 'Woda', 10.00)
basket.add_product(product, 5)
basket.count_total_price()
50.0
basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00'
"""

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price} PLN'

# p1_woda = Product(1, "Woda", 10)
# print(p1_woda)

class Basket:
    def __init__(self):
        # struktura słownika _items -> nazwa_produktu: ilość
        self._items = dict()

    def add_product(self, product: Product, quantity):
        if not isinstance(product, Product):
            raise TypeError('product should be instance of Product')

        if quantity <= 0:
            raise ValueError('quantity should be greater than zero')

        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity

    @property # powoduje, że metoda jest traktowana jak atrybut obiektu i coś zwraca
    def is_empty(self) -> bool:
        return not self._items

    def count_total_price(self):
        total_price = 0.0
        for product, quantity in self._items.items():
            total_price += product.price * quantity
        return total_price

    def generate_report(self):
        print("Produkty w koszyku:")
        for product, quantity in self._items.items():
            print(f'{product.name} ({product.id}), cena: {product.price:.2f} x {quantity}')
        print(f'Suma koszyka: {self.count_total_price():.2f}')


# koszyk = Basket()
# print( koszyk.is_empty )
# koszyk.add_product(p1_woda, 2)
# print(koszyk.is_empty)
# print( koszyk.count_total_price() )
# print()
# koszyk.generate_report()

import pytest
def test_1():
    koszyk = Basket()
    assert koszyk.is_empty == True
    assert len(koszyk._items) == 0

def test2():
    koszyk = Basket()
    jablko = Product(1, 'jablko', 2.59)
    koszyk.add_product(jablko, 10)
    assert koszyk.is_empty == False
    assert len(koszyk._items) == 1
    assert koszyk._items[jablko] == 10

def test3():
    koszyk = Basket()
    with pytest.raises(TypeError):
        koszyk.add_product('ala ma kota!', 100)

def test3():
    koszyk = Basket()
    gruszka = Product(2, 'gruszka', 5.50)
    with pytest.raises(ValueError):
        koszyk.add_product(gruszka, -1)

def test4():
    koszyk = Basket()
    sliwka = Product(3, 'śliwka', 2)
    koszyk.add_product(sliwka, 9)
    assert len(koszyk._items) == 1
    assert koszyk._items[sliwka] == 9

    koszyk.add_product(sliwka, 2)
    assert len(koszyk._items) == 1
    assert koszyk._items[sliwka] == 11

    assert koszyk.count_total_price() == 22

    wisnia = Product(4, 'wiśnia', 6)
    koszyk.add_product(wisnia, 1)
    assert koszyk.count_total_price() == 28