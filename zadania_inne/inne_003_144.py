# 1.4.4
# Napisz program, który wczytuje od użytkownika nieujemną liczbę całkowitą n i wypisuje liczbę n!.

liczba = int(input("Podaj liczbe nieujemną! "))

while liczba < 0:
    liczba = int(input("Podales liczbe mniejszą od zera. Jeszcze raz! "))

silnia = 1
for i in range(liczba):
    silnia = silnia + silnia * i
print(silnia)