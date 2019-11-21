# 1.4.6
# Napisz program, który wczytuje liczbę całkowitą n (n > 2)
# i wypisuje iloczyn liczb parzystych z zakresu od 2 do n
# (czyli 2 ∗ 4 ∗ ... ∗ n dla n parzystych oraz 2 ∗ 4 ∗ ... ∗ (n − 1) w przeciwnym wypadku).

n = int(input("Podaj liczbę całkowitą dodatnią większą od 2! "))

while not n > 2:
    n = int(input("Podales niepoprawną liczbę. Jeszcze raz! "))

iloczyn = 1
i = 2
while i <= n:
    iloczyn = iloczyn * i
    i = i + 2

print(iloczyn)

