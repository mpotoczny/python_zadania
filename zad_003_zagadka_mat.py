import random

### Zadanie 2.1 | Zagadka matematyczna
#
#Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby
# i pyta jaka jest ich suma (nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
#

# a = int(input("Podaj pierwsza liczbe z zakresu 0-99 "))
# b = int(input("Podaj drugą liczbe z zakresu 0-99 "))

a = random.randint(0,99)
b = random.randint(0,99)

print(a)
print(b)

suma = a + b

while True:

    zgaduj = int(input("Ile wynosi suma? "))

    if zgaduj == suma:
        print(f"Brawo, odgadłeś sumę. Wynosi ona {suma}!")
        break
    else:
        print("Podałeś niepoprawną sumę! Spróbuj jeszcze raz!")
        continue

