# zad 2.3
# Napisz program, który w pętli prosi o podanie kolejnego działania w formie jedne linii tekstu.
# Na podstawie dwóch podanych liczb oraz znaku operacji między nimi oblicza wynik działania matematycznego.
# Ustalmy, że aby zakończyć użytkownik wpisuje słowo koniec.
# Obsłuż co najmniej cztery podstawowe działania matematyczne (`+`, `-`, `*`, `/`).

l1 = int(input("Podaj pierwszą liczbę: "))
l2 = int(input("Podaj drugą liczbę: "))

while True:
    dzialanie = input("Podaj znak działania! ")

    if dzialanie == '+':
        print(f"Wynik dodawania to {l1+l2}")
        continue
    elif dzialanie == '-':
        print(f"Wynik odejmowania to {l1-l2}")
        continue
    elif dzialanie == '*':
        print(f"Wynik mnożenia to {l1*l2}")
        continue
    elif dzialanie == '/':
        print(f"Wynik dzielenia to {l1/l2}")
    elif dzialanie.upper() == 'KONIEC':
        break
    else:
        print("Podałeś nieprawidłowy znak. Spróbuj ponownie! ")
        continue
