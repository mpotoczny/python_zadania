# zad 2.4
# Napisz program, który odczytuje od użytkownika wiele liczb.
# Program powinien wyliczyć i na końcu wypisać następujące statystyki:
# - liczba podanych liczb (ile sztuk),
# - suma,
# - średnia,
# - minimum
# - maksimum

print("Program wylicza statystyki wprowadzonych liczb. W celu zakończenia wprowadzania naciśnij 'k'.")
lista = []

while True:
    x = (input("Podaj liczbę "))
    if x != 'k':
        x = int(x)
        lista.append(x)
    else:
        print(f"Suma: {sum(lista)}")
        print(f"Średnia: {sum(lista)/len(lista)}")
        print(f"Minimum: {min(lista)}")
        print(f"Maximum: {max(lista)}")
        break