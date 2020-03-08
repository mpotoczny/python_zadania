# Zadanie 4.1 | Ogłoszenia Zaproponuj klasę, w której obiektach
# będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).

class Ogloszenie:
    _next_id = 1 #atrybut klasowy

    def __init__(self, tytul, opis, cena, telefon, miejscowosc):
        self.id = Ogloszenie._next_id
        Ogloszenie._next_id += 1

        self.tytul = tytul
        self.opis = opis
        self.cena = cena
        self.telefon = telefon
        self.miejscowosc = miejscowosc

    def __str__(self):
        tresc = f'\nID: {self.id}\n' \
                f'{self.cena} PLN, {self.miejscowosc.upper()}, tel.: {self.telefon}, ' \
                f'{self.tytul.upper()}\n' \
                f'{self.opis}\n***'
        return tresc


ogl1 = Ogloszenie('pomoc domowa', 'Pomogę w domu przy zwierzętach i ludziach', 80, 123456, 'WrocłAW')
ogl2 = Ogloszenie('Katering na urodziny', 'Zrobie placków', 120, 22123456, 'kenia północna')

print(ogl1)
print(ogl2)