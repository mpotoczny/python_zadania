import sys
import collections

try:
    nazwa_pliku = sys.argv[1]
    print(nazwa_pliku, '\n')

    with open(nazwa_pliku, encoding='UTF8') as file:
        dane = file.read() # zmienna dane to string z zawartoscią wczytanego pliku
        print(dane)
        print('+' * 60)

        lista_zaw = dane.split('\n') # tworzy listę z elementami rozdzielonymi \n
        print(lista_zaw)
        print('+' * 60)

        lista_list = []
        for linia in lista_zaw:
            if len(linia) > 0:
                zawodnik = linia.split('\n')
                # print(zawodnik)
                for element in zawodnik:
                    dane_zawodnika = ( element.split(';') )
                    lista_list.append(dane_zawodnika)

        print(lista_list)
        print('+' * 60, end='\n\n')

except IndexError:
    print('Uruchomienie programu: python zad_5_1_a.py zawodnicy.csv')
    exit(1)

except FileNotFoundError:
    print(f'Plik {nazwa_pliku} nie odnaleziony!')
    exit(1)



#FUNKCJE

def ktojaki(lista_list_zaw: list):
    max_wzrost, min_wzrost, max_waga, min_waga = (None,)*4

    for lista in lista_list_zaw:
        wzrost = int(lista[4])
        waga = int(lista[5])

        if max_wzrost is None:
            max_wzrost = wzrost
        if min_wzrost is None:
            min_wzrost = wzrost
        if max_waga is None:
            max_waga = waga
        if min_waga is None:
            min_waga = waga

        if max_wzrost < wzrost:
            max_wzrost = wzrost
            imie_najw = lista[0]
            nazwisko_najw = lista[1]

        if min_wzrost > wzrost:
            min_wzrost = wzrost
            imie_najn = lista[0]
            nazwisko_najn = lista[1]

        if max_waga < waga:
            max_waga = waga
            imie_najc = lista[0]
            nazwisko_najc = lista[1]

        if min_waga > waga:
            min_waga = waga
            imie_najl = lista[0]
            nazwisko_najl = lista[1]

    print(f"Najwyższy to {imie_najw} {nazwisko_najw}: {max_wzrost} cm")
    print(f"Najniższy to {imie_najn} {nazwisko_najn}: {min_wzrost} cm")
    print(f"Najcięższy to {imie_najc} {nazwisko_najc}: {max_waga} kg")
    print(f"Najlżejszy to {imie_najl} {nazwisko_najl}: {min_waga} kg")
    print('+' * 60, end='\n\n')


def suma_wag_zawodnikow(lista_list_zaw:list):

    kraje = set()
    for lista in lista_list_zaw:
        kraje.add(lista[2]) # dodanie nazw krajów. Zbiór posiada wartości unikatowe, więc każdy kraj bedzie tylko 1 raz
    print(kraje)

    kraj = input("Ważenie zawodników: podaj kraj! ")
    kraj = kraj.upper()

    if kraj not in kraje:
        raise ValueError("Brak skoczków z tego kraju.")

    suma_wag = 0
    for lista in lista_list_zaw:
        if lista[2] == kraj:
            waga = int(lista[5])
            suma_wag += waga
    print(f'Suma wag skoczków z kraju {kraj} wynosi {suma_wag} kg!')
    print('+' * 60, end='\n\n')

def ilosc_i_wzrost_z_kraju(lista_list_zaw:list):
    ilu_skad = collections.defaultdict(int)
    suma_wzrostow = collections.defaultdict(int)

    for lista in lista_list_zaw:
        ilu_skad[ lista[2] ] += 1

    print('ilu skad: ', ilu_skad)

    for kraj, ilosc in ilu_skad.items():
        print(f'{kraj} - {ilosc}')

    print('+' * 60, end='\n\n')

    for lista in lista_list_zaw:
        wzrost = int(lista[4])
        kraj = lista[2]
        suma_wzrostow[kraj] += wzrost

    print('suma_wzrostow: ', suma_wzrostow)
    print()

    kraje = list(ilu_skad.keys())
    ilosc_zaw = list(ilu_skad.values())
    wzrosty = list(suma_wzrostow.values())

    print(kraje)
    print(ilosc_zaw)
    print(wzrosty)
    print()

    sredni_wzrost = [ x/y for x,y in zip(wzrosty, ilosc_zaw) ]
    # print(sredni_wzrost)

    wynik = zip(kraje, sredni_wzrost)
    for kraj, srednia in wynik:
        print(f'{kraj} - {srednia:.2f} cm')

    print('+' * 60, end='\n\n')


# wywołania funkcji
ktojaki(lista_list)
ilosc_i_wzrost_z_kraju(lista_list)
suma_wag_zawodnikow(lista_list)

