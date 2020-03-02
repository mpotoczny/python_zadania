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

p1 = Product(1, "Woda", 10)
print(p1)

class Basket:
    def __init__(self):
        # struktura słownika items -> nazwa_produktu: ilość
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



