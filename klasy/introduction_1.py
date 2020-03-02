class Towar:
    pass

a = Towar()

a.nazwa ="Żyletki"
a.cena = 6.00

print(f'{a.nazwa}, {a.cena:.2f}')
print(a.nazwa, a.cena)

class Towar:
    def wypisz_sie(self):
        print(f'Towar {self.nazwa} kosztuje {self.cena:.2f} waluty!')

x = Towar()
x.nazwa  = "Agrafka"
x.cena = 10.5
print(x)
x.wypisz_sie()

print("*" * 60)

class Towar:
    def __init__(self, nazwa="coś", cena=10):
        self.nazwa = nazwa
        self.cena = cena

    def __str__(self):
        return f'Towar {self.nazwa} kosztuje {self.cena} waluty!'


y = Towar()
print(y.nazwa, y.cena) # nazwa i cena zyskały argumenty domyślne, podane w konstruktorze
print(y)

# y_txt = str(y)
# print(y_txt)

print("*" * 60)

class Matematyka:
    PI = 3.14 # atrybut klasowy, z idei - niezmienny

print(Matematyka.PI)

print("*" * 60)
# FUNKCJA RANGE - PRZYPOMNIENIE

# funkcja range jest prawostronnie otwarta, czyli nie bierze w zakres ostatniego elementu
# i domyślnie startuje od zera
list1 = list (range(5) ) # [0, 1, 2, 3, 4]
list2 = list( range(0,5) ) # [0, 1, 2, 3, 4]
list3 = list( range(1,10) ) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
print(list2)
print(list3)
print("*" * 60)

cells = [" "] * 5
print(cells)

print("*" * 60)

def stopifZero(a):
    if int(a) == 0:
        return True
    else:
        return False

while True:
    if stopifZero(input('Number ')) is True:
        break
    else:
        continue







