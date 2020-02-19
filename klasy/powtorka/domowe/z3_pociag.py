class Pociag:

    def __init__(self, predkosc:int=10, ilosc_paliwa:int=1000):
        self.predkosc = predkosc
        self.ilosc_paliwa = ilosc_paliwa

    def opis(self):
        return f'Moja predkosc to {self.predkosc}. Mam jeszcze {self.ilosc_paliwa} litrow paliwa.'

    def __str__(self):
        return f'Moje dane to: {self.predkosc} km/h, {self.ilosc_paliwa} l.'

p1 = Pociag()
# print(p1.predkosc, p1.ilosc_paliwa)
print( Pociag.opis(p1) ) #dostęp do metody opis za pomocą nazwy klasy i kropki
print(p1)