# ==== ABSTRAKCJA =====
# modul ABC (Abstract Base Class)
# żeby oznaczyć klasę jako abstrakcyjną, to ta klasa ma dziedziczyc po ABC (Abstract Base Class)
# te metody w klasie abstrakcyjnej, co do ktorych nie wiemy jak maja dzialac
# oznaczamy dekoratorem @abstractmethod

# dekoratorem @abstractmethod oznaczmy metdoę, o której nie wiemy jak będzie działać
# metoda abstrakcyjna, to taka której działanie moze różnić się w klasach-dzieciach
# a jest 'deklarowana' również w klasie-rodzicu


from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Discount(ABC):
    def __init__(self, amount):
        self._amount = amount

    @abstractmethod
    def calculate(self, total_price):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

class ValueDiscount(Discount):
    def calculate(self, total_price):
        return total_price - self._amount

    def __add__(self, other):
        return ValueDiscount(self._amount + other._amount)

class PercentageDiscount(Discount):
    def calculate(self, total_price):
        return total_price - total_price * self._amount / 100.0

    def __add__(self, other):
        return PercentageDiscount(self._amount + other._amount)


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_info(self):
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN'

    def print_info(self):
        print(f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN')

    def __str__(self):
        return self.get_info()


class Basket:
    def __init__(self):
        self._items = dict()
        self._discounts = []

    def add_discount(self, discount: Discount):
        self._discounts.append(discount)

    def add_product(self, product: Product, quantity: int = 1):
        if not isinstance(product, Product):
            raise TypeError('product has to be instance of Product')

        if quantity <= 0:
            raise ValueError('quantity has to be greater than 0')

        if product in self._items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity

    @property
    def is_empty(self) -> bool:
        return not self._items

    def count_total_price(self):
        basket_total_price = sum( [ product.price * quantity for product, quantity in self._items.items() ] )

        sum_vd = ValueDiscount(0)
        sum_pd = PercentageDiscount(0)

        for discount in self._discounts:
            if isinstance(discount, ValueDiscount):
                sum_vd += discount
            elif isinstance(discount, PercentageDiscount):
                sum_pd += discount

        basket_total_price = sum_vd.calculate(basket_total_price)
        basket_total_price = sum_pd.calculate(basket_total_price)

        # if basket_total_price < 0:
        #     return 0
        # else:
        #     return basket_total_price

        return basket_total_price if basket_total_price >= 0 else 0

    def generate_report(self):
        print("Produkty w koszyku:")
        for product, quantity in self._items.items():
            print(f'{product.name} ({product.id}), cena: {product.price:.2f} x {quantity}')
        print(f'W sumie: {self.count_total_price():.2f}')

    @classmethod
    def with_products(cls, products):
        basket = cls()
        for product in products:
            basket.add_product(product)
        return basket


pr1 = Product(1, "Jablka", 10)
pr2 = Product(2, "Morele", 20)

koszyk = Basket.with_products([pr1, pr2])

koszyk.count_total_price() == 30

vd1 = ValueDiscount(5)
vd2 = ValueDiscount(5)
pd1 = PercentageDiscount(10)
pd2 = PercentageDiscount(10)

print(type(pr1))
print(type(vd1))
print(type(pd1))
print(type(pd1) == Discount)


koszyk.add_discount(vd1)
koszyk.add_discount(vd2)
koszyk.add_discount(pd1)
koszyk.add_discount(pd2)

print()
print( koszyk.count_total_price() )










