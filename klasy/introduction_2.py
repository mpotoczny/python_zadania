class Osoba:
    def __init__(self, imie, nazwisko, id):
        self.imie = imie # public
        self._nazwisko = nazwisko # protected
        self.__id = id # private

piotrek = Osoba('Piotr', 'GG', 100)
print(piotrek.imie)
print(piotrek._nazwisko)
print(piotrek.__id)  #name mangling
print(piotrek._Osoba__id)
