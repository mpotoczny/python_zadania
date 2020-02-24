class Pociag:

    def __init__(self, predkosc:int=10, ilosc_paliwa:int=1000):
        self.predkosc = predkosc
        self.ilosc_paliwa = ilosc_paliwa

    def opis(self):
        return f'Moja predkosc to {self.predkosc}. Mam jeszcze {self.ilosc_paliwa} litrow paliwa.'

    def __str__(self):
        return f'Moje dane to: {self.predkosc} km/h, {self.ilosc_paliwa} l.'

    def przyspiesz(self, przyrost:int):
      #  stara_predkosc = self.predkosc
      #  self.predkosc = self.predkosc + przyrost
      #  temp_predkosc = self.predkosc

      stara_predkosc = self.predkosc

      if self.ilosc_paliwa != 0:
          temp_predkosc = self.predkosc + przyrost
          if temp_predkosc <= stara_predkosc * 1.75:
              self.predkosc = temp_predkosc

      nowa_predkosc = self.predkosc

      self.ilosc_paliwa =  self.ilosc_paliwa - (nowa_predkosc - stara_predkosc) * (stara_predkosc / 100)

p1 = Pociag()
# print(p1.predkosc, p1.ilosc_paliwa)
# print( Pociag.opis(p1) ) #dostęp do metody opis za pomocą nazwy klasy i kropki. Metoda wywolana na obiekcie p1
print(p1)

p1.przyspiesz(5)
print(p1)