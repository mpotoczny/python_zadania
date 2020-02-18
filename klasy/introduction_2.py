class Osoba:
    def __init__(self, imie, nazwisko, id):
        self.imie = imie # public
        self._nazwisko = nazwisko # protected
        self.__id = id # private

# piotrek = Osoba('Piotr', 'GG', 100)
# print(piotrek.imie)
# print(piotrek._nazwisko)
# # print(piotrek.__id)  #name mangling
# print(piotrek._Osoba__id)

class Osoba:
    def __init__(self, nazwisko, id):
        self._nazwisko = nazwisko
        self.__id = id

    def get_nazwisko(self):
        return self._nazwisko

    def set_nazwisko(self, nazwisko):
        self._nazwisko = nazwisko

    def get_id(self):
        return self.__id

# piotrek = Osoba('GG', 1)
# print(piotrek.get_nazwisko())
# piotrek.set_nazwisko("Kowal")
# print(piotrek.get_nazwisko())

class Osoba:
    def __init__(self, nazwisko, id):
        self.nazwisko = nazwisko

    @property
    def nazwisko(self): # getter
        print("Jestem w geterze")
        return self._nazwisko

    @nazwisko.getter
    def nazwisko(self):
        print(123)

    @nazwisko.setter
    def nazwisko(self, nowe_nazwisko):
        print("Jestem w setterze")
        self._nazwisko = nowe_nazwisko


janusz = Osoba('Kowalski', 2)
print(janusz.nazwisko)
