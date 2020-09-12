"""
Napisz program zliczający liczbę wystąpień każdego znaku
w podanym przez użytkownika napisie.
"""

napis = input("Czekam na podanie napisu. ")
wystapienia = {}   # pusty słownik

for znak in napis.lower():
    if znak not in wystapienia:
        wystapienia[znak] = 0

    wystapienia[znak] += 1


for litera, liczba_wystapien in wystapienia.items():
    print(f'{litera} - {liczba_wystapien}')
