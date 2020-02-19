lista_obj = []

class Ogloszenie:
    _next_id = 1 #atrybut klasowy

    def __init__(self, model, opis, cena, telefon, miejscowosc):
        self.id = Ogloszenie._next_id
        Ogloszenie._next_id += 1 #zwiekszane przy każdym użyciu

        self.model = model
        self.opis = opis
        self.cena = cena
        self.telefon = telefon
        self.miejscowosc = miejscowosc

        lista_obj.append(self) #dodanie obiektu do listy

    def __str__(self):
        tresc = f'\nID: {self.id}\n' \
                f'{self.model.upper()} {self.cena} PLN, {self.miejscowosc.upper()}, ' \
                f'tel.: {self.telefon}\n' \
                f'{self.opis}\n***'
        return tresc

car1 = Ogloszenie('Opel ASTRA', '3-letni', 10000, 1234566, 'Ząbki')
car2 = Ogloszenie('Honda Jazz', 'Powypadkowy', 20000, 1234343, 'Warszawa')
car3 = Ogloszenie('Fiat Punto', 'Nowy', 50000, 122234343, 'Garwolin')
car4 = Ogloszenie('Seat Leon', 'Diesel/LPG', 45750, 7643222, 'Ząbki')

print(lista_obj)

# lista_modeli = []
# for obiekt in lista_obj:
#     lista_modeli.append(obiekt.model)
# print(lista_modeli)

# ***
# Ogłoszenia z przedziału cenowego 40000-50000

#wybranie/filtracja po warunku. Utworzenie listy obiektów-ogłoszeń, które spełniają warunek
obiekty_w_przedziale = list( filter(lambda obiekt: obiekt.cena>40000, lista_obj) )
print(obiekty_w_przedziale)

# utworzenie listy z modelami spełniającymi warunek
modele_z_przedzialu = []
for obiekt in obiekty_w_przedziale:
    modele_z_przedzialu.append(obiekt.model)
print(modele_z_przedzialu)

#słownik
from collections import defaultdict

# utworzenie słownika model-cena z ogłoszeń spełniających warunek
slownik_z_modelami = {}
for obiekt in obiekty_w_przedziale:
    slownik_z_modelami[obiekt.model] = obiekt.cena
print(slownik_z_modelami)