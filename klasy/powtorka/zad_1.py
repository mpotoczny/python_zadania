"""
Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu. Zaimplementuj metodę wypisującą informację o produkcie na konsolę.
Przykład użycia:
product = Product(1, 'Woda', 10.99)
product.print_info()
Produkt "Woda", id: 1, cena: 10.99 PLN
"""

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        
    def info(self):
        info_txt = f'Product: {self.name}, price: {self.price} USD, id: {self.id}'
        print(info_txt)

p1 = Product(1, 'Water', 10.99)
p1.info()
p2 = Product(2, 'Sausage', 20)
p2.info()

