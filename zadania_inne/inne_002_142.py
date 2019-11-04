# 1.4.2
# Napisz program wczytujący od użytkownika dwie dodatnie liczby całkowite n i m,
# i wypisujący m pierwszych wielokrotności liczby n.

n = int(input("Podaj całkowitą dodatnią liczbę n: "))
m = int(input("Podaj całkowitą dodatnią liczbę m: "))

while n <= 0:
    n = int(input("Podana liczba n była niedodatnia. Jeszcze raz! "))
while m <= 0:
    m = int(input("Podana liczba m była niedodatnia. Jeszcze raz! "))

n1 = n
for ile in range(m):
    print(n1)
    n1 = n1 + n