class Ogloszenie:
    _next_id = 1

    def __init__(self, tytul, opis, cena, telefon, miejscowosc):
        self.id = Ogloszenie._next_id
        Ogloszenie._next_id += 1

        self.tytul = tytul
        self.opis = opis
        self.cena = cena
        self.telefon = telefon
        self.miejscowosc = miejscowosc

    def __str__(self):
        tresc = f'\n***\nId: {self.id}, {self.tytul}\n***\n{self.opis}\n***\nCena: {self.cena}\n***\nMiejscowość: {self.miejscowosc}\n***\nTel.: {self.telefon}\n***'

        return tresc



ogl1 = Ogloszenie('KOMPUTER','PC najnowszej generacji, używany', 200, '123456','Kraków')
ogl2 = Ogloszenie('BLENDER','Miksowacz nowy', 500, '121456','Kraków')

print(ogl1)
print(ogl2)