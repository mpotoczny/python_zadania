"""
Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.
Ma ona mieć metody:
`dodaj_element(x: int, y: int, rodzaj_elementu)`
W argumencie `rodzaj_elementu` będzie napis `“x”` lub `“y”`. Jeśli ruch jest nieprawidłowy, metoda powinna zwracać fałsz.
`stan_gry()`
Ta metoda ma zwracać liczbę oznaczającą stan gry (gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona sukcesem kółek).
`czyj_ruch()`
Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).
Wyświetlenie obiektu tej klasy ma wypisać planszę.
Użyj tej klasy do zrobienia gry w kółko i krzyżyk.
"""
class PlanszaXO:
    LICZBA_POL = 9
    PUSTE_POLE = " "
    def __init__(self):
        self.plansza = []
    def zainicjalizuj_gre(self):
        for pole in range(PlanszaXO.LICZBA_POL):
            self.plansza.append(PlanszaXO.PUSTE_POLE)
    def stan_gry(self):
        self.zwyciezca = None
        self.koniec = ((0,1,2),
                       (3,4,5),
                       (6,7,8),
                       (0,3,6),
                       (1,4,7),
                       (2,5,8),
                       (0,4,8),
                       (2,4,6))
        for kolumna in self.koniec:
            if self.plansza[kolumna[0]] == self.plansza[kolumna[1]] == self.plansza[kolumna[2]] != PlanszaXO.PUSTE_POLE:
                self.zwyciezca = self.plansza[kolumna[0]]
                print (self.zwyciezca)
            elif PlanszaXO.PUSTE_POLE not in self.plansza:
                print ('REMIS!')
            else:
                return None
    def gracze(self, x, y):
        self.mozliwy_ruch = []
        self.x = x
        self.y = y
        self.kolej_ruchu = self.x
        for pole in range(PlanszaXO.LICZBA_POL):
            if self.plansza[pole] == PlanszaXO.PUSTE_POLE:
                self.mozliwy_ruch.append(pole)


    def wybor_ruchu(self):
        ruch = None
        while ruch not in self.mozliwy_ruch:
            if self.kolej_ruchu == self.x:
                ruch = int(input("Jaki będzie Twój ruch X?"))
            elif self.kolej_ruchu == self.y:
                ruch = int(input("Jaki będzie Twój ruch Y?"))
                if ruch not in self.mozliwy_ruch:
                    print ("To pole jest juz zajęte, lub nie ma takiego pola")
        self.plansza[ruch] = self.kolej_ruchu
        self.mozliwy_ruch.remove(ruch)
        return self.plansza

    def czyj_ruch(self):
        if self.kolej_ruchu == self.x:
            self.kolej_ruchu = self.y
        else:
            self.kolej_ruchu = self.x


    def __str__(self):
        return f'{self.plansza[0]} | {self.plansza[1]} | {self.plansza[2]}\n' \
               f'---------\n' \
               f'{self.plansza[3]} | {self.plansza[4]} | {self.plansza[5]}\n' \
                f'---------\n' \
                f'{self.plansza[6]} | {self.plansza[7]} | {self.plansza[8]}'

def main():
    gramy = PlanszaXO()
    gramy.zainicjalizuj_gre()
    print (gramy)
    gramy.gracze("X","Y")
    while not gramy.stan_gry():
        gramy.wybor_ruchu()
        gramy.czyj_ruch()
        print(gramy)

main()