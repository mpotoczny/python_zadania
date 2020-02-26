class Zolw:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kurs = 0

    #obrot dla 4 kierunkow swiata, zgodnie z kierunkiem ruchu zegara
    def idz(self, odleglosc):
        if self.kurs == 90:
            self.x -= odleglosc
        elif self.kurs == 180:
            self.y += odleglosc
        elif self.kurs == 270:
            self.x += odleglosc
        else: # zawiera warunek gdy self.kurs == 0
            self.y -= odleglosc

    def obroc_sie(self, obrot:0):
        self.kurs = obrot

    def __str__(self):
        return f'x={self.x}, y={self.y}, kurs={self.kurs}'

zw1 = Zolw(100,100)
print(zw1)
zw1.idz(50)
print(zw1)
zw1.obroc_sie(90)
zw1.idz(50)
print(zw1)



