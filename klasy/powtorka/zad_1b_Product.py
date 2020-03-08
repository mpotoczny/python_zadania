class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_info(self):
        return f'product: {self.name}, price: {self.price} USD, ID: {self.id}'

    def print_info(self):
        print(f'product: {self.name}, price: {self.price} USD, ID: {self.id}')

    def __str__(self):
        return self.get_info()

# p1 = Product(3, "Whisky", 200)
# print(p1)


def test_no1():
    woda = Product(1, "Woda", 2.49)
    assert woda.id == 1
    assert woda.name == "Woda"
    assert woda.price == 2.49

def test_no2():
    woda = Product(1, "Woda", 2.49)
    info = woda.get_info()
    assert info == "product: Woda, price: 2.49 USD, ID: 1"


def test_no3(capsys):
    woda = Product(1, "Woda", 2.49)
    woda.print_info()

    out, err = capsys.readouterr()
    assert out == "product: Woda, price: 2.49 USD, ID: 1\n"

def test_no4():
    perfumka = Product(2, "Luca", 500)
    assert str(perfumka) == 'product: Luca, price: 500 USD, ID: 2'









