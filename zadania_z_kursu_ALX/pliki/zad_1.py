"""
Napisz program wypisujący na konsolę zawartość wskazanego pliku
wraz z numerami linii. Obsłuż sytuację, gdy użytkownik nie poda nazwy pliku
lub poda błędną nazwę.
Przykład użycia:
$ python test.txt
1: pierwsza linia pliku
2: druga linia pliku
"""

# zeby uruchomic ten program, w terminalu wpisz:
# python zad_1.py plik.txt

import sys

# sys_argv[1] zwraca nazwę pierwszego argumentu przekazywanego do programu (pliku)
# sys_argv[0] to nazwa/ścieżka do uruchamianego programu
file_name = sys.argv[1]

try:
    with open(file_name) as file:
        dane = file.read()

        #1
        line_number = 1
        for line in dane.split('\n'):
            print(f'{line_number}: {line}')
            line_number += 1
        print('-' * 60, '\n')

        #2
        for line_number, line in enumerate(dane.split('\n'), start=1):
            print(f'{line_number}: {line}')
        print('-' * 60, '\n')

        #3
        file.seek(0)
        line_number = 1
        while True:
            line = file.readline()
            if not line:
                break
            print(f'{line_number}: {line}')
            line_number += 1
        print('-' * 60, '\n')

        #4
        file.seek(0)
        dane = file.readlines()

        print(dane) # lista linii, ignoruje ostatnią pustą linię
        print( type(dane) )
        print()

        for line_number, line in enumerate(dane, start=1):
            print(f'{line_number}: {line}')
        print('-' * 60, '\n')

        #5
        file.seek(0)
        for line_number, line in enumerate(file, start=1):
            print(f'{line_number}: {line}')
        print('-' * 60, '\n')






except IndexError:
    print(f'uzycie programu: python zad_1.py file.txt')
    exit(1)

except FileNotFoundError:
    print('Nie znaleziono pliku.')
    exit(1)

