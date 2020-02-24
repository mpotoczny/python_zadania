class Pociag:

    def __init__(self, predkosc:int=10, ilosc_paliwa:int=1000):
        self.predkosc = predkosc
        self.ilosc_paliwa = ilosc_paliwa

    def opis(self):
        return f'Moja predkosc to {self.predkosc}. Mam jeszcze {self.ilosc_paliwa} litrow paliwa.'

    def __str__(self):
        return f'Moje dane to: {self.predkosc:.1f} km/h, {self.ilosc_paliwa:.2f} l.'

    def przyspiesz(self, przyrost:int):

      stara_predkosc = self.predkosc

      if self.ilosc_paliwa != 0: # wykonuje się gdy jest jeszcze paliwo przed przyrostem
          temp_predkosc = self.predkosc + przyrost
          if temp_predkosc <= stara_predkosc * 1.75: # jeśli predkosc z przyrostem nie przekracza 175% Vo
              self.predkosc = temp_predkosc # to przyspiesz, jesli przekracza self.predkosc zostaje bez zmian

      nowa_predkosc = self.predkosc

      # formuła z treści do obliczenia spalania paliwa
      nowa_ilosc_paliwa =  self.ilosc_paliwa - (nowa_predkosc - stara_predkosc) * (stara_predkosc / 100)
      if nowa_ilosc_paliwa > 0: # jeśli po obliczeniach zostanie paliwo to przyspiesz
          self.ilosc_paliwa = nowa_ilosc_paliwa
      else: # jeśli paliwa nie zostanie to nic nie zmieniaj (nie przyspieszaj)
          self.predkosc = stara_predkosc

# p1 = Pociag()
# # print(p1.predkosc, p1.ilosc_paliwa)
# # print( Pociag.opis(p1) ) #dostęp do metody opis za pomocą nazwy klasy i kropki.
# # Metoda wywolana na obiekcie p1
# print(p1)
#
# p1.przyspiesz(5)
# print(p1)
#
# p1.przyspiesz(6)
# print(p1)
# p1.przyspiesz(10)
# print(p1)
# p1.przyspiesz(67)
# print(p1)
# p1.przyspiesz(0)
# print(p1)
#
# p2 = Pociag(10,8)
# print(p2)
# p2.przyspiesz(4)
# print(p2)
# p2.przyspiesz(10)
# print(p2)
# p2.przyspiesz(15)
# print(p2)
# p2.przyspiesz(20)
# print(p2)
# p2.przyspiesz(5)
# print(p2)
# p2.przyspiesz(1.4)
# print(p2)

def test1():
    p1 = Pociag() #domyślne to 10 km/h, 1000 l
    p1.przyspiesz(5)
    assert p1.predkosc == 15
    assert str(p1) == "Moje dane to: 15.0 km/h, 999.50 l."

def test2():
    p1 = Pociag(55, 80)
    p1.przyspiesz(20)
    assert p1.predkosc == 75
    assert str(p1) == "Moje dane to: 75.0 km/h, 69.00 l."