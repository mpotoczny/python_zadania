# iterator w klasach pochodnych

class Product:
    _next_id = 1

    def __init__(self, name, price):
        self.id = Product._next_id
        Product._next_id += 1

        self.name = name
        self.price = price

    def print_info(self):
        print(f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN')

    def get_info(self):
        return f'Produkt "{self.name}", id: {self.id}, cena: {self.price:.2f} PLN'

    def __str__(self):
        return self.get_info()

class ProductPremium(Product):
    def __init__(self, name, price):
        self.id = ProductPremium._next_id
        Product._next_id += 1

        self.name = name
        self.price = price

p1 = Product('jeden', 123)
p2 = ProductPremium('dwa', 456)
p3  = Product('trzy', 789)
p4 = ProductPremium('cztery', 101112)
p5  = Product('pięć', 131415)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)