# 1.4.1
# Napisz program wczytujący od użytkownika dwie liczby całkowite n i m,
# i wypisujący w kolejnych wierszach wszystkie wielokrotności n mniejsze od m.

while True:

    n = int(input("Podaj całkowitą liczbę n: "))
    m = int(input("Podaj całkowitą liczbę m: "))

    if n > m:
        print("Liczba n jest większa od m. Jeszcze raz!")
        continue
    else:
        n1 = n
        while n1 < m:
                print(n1)
                n1 = n1 + abs(n)
    break

