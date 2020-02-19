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

    def __str__(self):
        tresc = f'\nID: {self.id}\n' \
                f'{self.model.upper()} {self.cena} PLN, {self.miejscowosc.upper()}, ' \
                f'tel.: {self.telefon}\n' \
                f'{self.opis}\n***'
        return tresc

car1 = Ogloszenie('Opel ASTRA', 'Sprawny', 10000, 1234566, 'Ząbki')
car2 = Ogloszenie('Honda Jazz', 'Powypadkowy', 20000, 1234343, 'Warszawa')
car3 = Ogloszenie('Fiat Punto', 'Nowy', 50000, 122234343, 'Garwolin')
print(car1, car2, car3)

