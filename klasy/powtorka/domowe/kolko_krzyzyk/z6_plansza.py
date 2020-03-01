class PlanszaXO:
    PUSTE_POLE = " "
    ZAKRES_POL = range(0,10) # gra 3x3, pola od 1 do 9

    def __init__(self):
        self.plansza = []

    def start_gry(self): # inicjalizacja planszy pustymi polami (pustej planszy)
        for pole in range(9):
            self.plansza.append(PlanszaXO.PUSTE_POLE)

    def stan_gry(self):
        self.zwyciezca = None

        # w tym ułożeniu tych samych znaków gra się kończy
        # self.koniec_gry = ( (1,2,3),
        #                     (4,5,6),
        #                     (7,8,9),
        #                     (1,4,7),
        #                     (2,5,8),
        #                     (3,6,9),
        #                     (1,5,9),
        #                     (3,5,7) )


        self.koniec_gry = ((0,1,2),
                       (3,4,5),
                       (6,7,8),
                       (0,3,6),
                       (1,4,7),
                       (2,5,8),
                       (0,4,8),
                       (2,4,6))

        # sprawdzenie dla każdego ułożenia kończącego grę, czy znajduje się ono w planszy
        # czyli czy np. plansza[2] == plansza[5] == plansza[8] (i czy pola te nie są puste)
        for ulozenie in self.koniec_gry:
            if self.plansza[ulozenie[0]] == self.plansza[ulozenie[1]] == self.plansza[ulozenie[2]] != PlanszaXO.PUSTE_POLE:
                self.zwyciezca = self.plansza[ulozenie[0]] # zwycięzcą zostaje ten kto jest w tym polu
                print(self.zwyciezca)
            elif PlanszaXO.PUSTE_POLE not in self.plansza:
                print("REMIS!")
            else:
                return None

        # if self.zwyciezca == "X":
        #     print("Zwycięstwo X!")
        #     return 1
        # elif self.zwyciezca == "Y":
        #     print("Zwycięstwo Y!")
        #     return 2
        # elif self.zwyciezca == "":
        #     print("Remis!")
        #     return 0
        # else:
        #     return -1

    def gracze(self, x="X", y="Y"):
        self.x = x
        self.y = y
        self.wolne_pola = []
        self.kolej_ruchu  = self.x

        for pole in range(9):
            if self.plansza[pole] == PlanszaXO.PUSTE_POLE:
                self.wolne_pola.append(pole)

    def wybor_ruchu(self):
        ruch = None
        while ruch not in self.wolne_pola:
            if self.kolej_ruchu == self.x:
                ruch = int(input("Jaki będzie Twój ruch X?"))
            elif self.kolej_ruchu == self.y:
                ruch = int(input("Jaki będzie Twój ruch Y?"))
                if ruch not in self.wolne_pola:
                    print("To pole jest juz zajęte lub nie ma takiego pola")
        self.plansza[ruch] = self.kolej_ruchu
        self.wolne_pola.remove(ruch)
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


gramy = PlanszaXO()
gramy.start_gry()
print(gramy)
gramy.gracze("X", "Y")

while not gramy.start_gry():
    gramy.wybor_ruchu()
    gramy.czyj_ruch()
    print(gramy)