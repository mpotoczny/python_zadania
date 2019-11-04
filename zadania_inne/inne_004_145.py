# 1.4.5
# Napisz program, który wczytuje nieujemną liczbę całkowitą n
# i wypisuje sumę kwadratów liczb od 0 do n, czyli wartość 0^2 + 1^2 + 2^2 + ... + n^2.

liczba = int(input("Podaj liczbe nieujemną! "))

while liczba < 0:
    liczba = int(input("Podales liczbe mniejszą od zera. Jeszcze raz! "))

suma = 0
for i in range(liczba + 1):
    suma = suma + i**2
print(suma)