# zad 2.2
# Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę
# wypisuje w tylu liniach "choinkę" ze znaków `*`.

wysokosc = int(input("Podaj wysokość choinki w piętrach: "))

for i in range(wysokosc):
    print(' ' * (wysokosc - i - 1) + '*' * (2 * i + 1))

#opis z zajęć
# while i < n
#     " " -> * (n-i-1)
#     "*" -> * (i*2+1)