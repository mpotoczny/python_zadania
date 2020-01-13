'''
wczytuje dane z pliku csv za pomoca funkcjio csv.reader
tworzy z csv listę list na podstawie podanego separatora (delimiter)
'''

import sys
import csv

try:
    nazwa_pliku = sys.argv[1]
    print(nazwa_pliku)

    with open(nazwa_pliku) as file:
        dane = csv.reader(file, delimiter=';')

        lista_list =[]
        for wiersz in dane:
            lista_list.append(wiersz)

        print(lista_list)




except IndexError:
    print('Uruchomienie programu: python zad_5_1_csv.py zawodnicy1.csv')
    exit(1)

except FileNotFoundError:
    print(f'Plik {nazwa_pliku} nie odnaleziony!')
    exit(1)