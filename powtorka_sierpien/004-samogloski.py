"""
Napisz program zliczający liczbę wystąpień samogłosek
(a, e, i, o, u, y) w podanym przez użytkownika napisie.
"""

napis = input("podaj napis: ")
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
ile_samoglosek = 0

for znak in napis:
    if znak.lower() in samogloski:
        ile_samoglosek += 1

print(f"Ilosc samoglosek: {ile_samoglosek}")