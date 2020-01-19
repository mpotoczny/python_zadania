#  Napisz funkcję, która otrzymuje jako argumenty: dodatnią liczbę całkowitą n
#  oraz dwie n-elementowe listy przechowujące dwuwymiarowe wektory.
# Funkcja powinna zwracać sumę iloczynów skalarnych wektorów
# (iloczyn wektora 1 z listy 1 oraz wektora 1 z listy 2
# dodać iloczyn wektora 2 z listy 1 oraz wektora 2 z listy 2 itd.).

import random

def iloczyn_skalarny(n:int, lista1: list, lista2: list) -> float:
    print(lista1)
    print(lista2)

    wynik = 0
    i = 0
    # j = 0

    while True:
        # skladowy_wynik1 = lista1[i][j]*lista2[i][j] + lista1[i][int(not j)]*lista2[i][int(not j)]
        skladowy_wynik = lista1[i][0]*lista2[i][0] + lista1[i][1]*lista2[i][1]
        wynik = wynik + skladowy_wynik
        i = i + 1

        # print( n == len(lista1) == len(lista2) )
        if i >= n:
            break
    return wynik

try:
    n = int(input('Podaj liczbę całkowitą - ilość wektorów w każdej liście: '))
    if n <= 0:
        raise ValueError

except ValueError:
    print('Wprowadzono niepoprawną daną.')
    exit(1)


lista1 = []
lista2 = []

for element in range(n):
    # losowanie współrzędnych wektorów w zakresie -100 do 100
    x1 = round( random.uniform(-100.0, 100.0), 2)
    x2 = round( random.uniform(-100.0, 100.0), 2)
    y1 = round( random.uniform(-100.0, 100.0), 2)
    y2 = round( random.uniform(-100.0, 100.0), 2)

    podlista1 = [x1, y1]
    podlista2 = [x2, y2]

    lista1.append(podlista1)
    lista2.append(podlista2)

wynik = iloczyn_skalarny(n, lista1, lista2)
print(f'Iloczyn skalarny wektorów wynosi {wynik:.2f} !')