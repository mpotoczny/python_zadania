import sys

try:
    nazwa_pliku = sys.argv[1]
    print(nazwa_pliku, '\n')

    with open(nazwa_pliku, encoding='UTF8') as file:
        dane = file.read() # zmienna dane to string z zawartoscią wczytanego pliku
        # print(dane)
        print('+' * 60)

        lista_zaw = dane.split('\n')
        # print(lista_zaw)
        # print('+' * 60)

        lista_list = []
        for linia in lista_zaw:
            if len(linia) > 0:
                zawodnik = linia.split('\n')
                for element in zawodnik:
                    dane_zawodnika = ( element.split(';') )
                    lista_list.append(dane_zawodnika)


        print(lista_list)
        print('+' * 60)

        # lista_list.sort(reverse=True, key=lambda x: x[4])
        # print(lista_list)

        # najwyzszy = max( map (lambda x: x[4], lista_list) )
        # highest = max( map(lambda x: x[4], lista_list))


    def najwyzszy(lista_list: list):
        max_wzrost = None
        for lista in lista_list:
            lista[4] = int(lista[4])
            if max_wzrost is None:
                max_wzrost = lista[4]
            elif lista[4] > max_wzrost:
                max_wzrost = lista[4]
                imie = lista[0]
                nazwisko = lista[1]

        print(f"Najwyższy to {imie} {nazwisko}")

    najwyzszy(lista_list)


except IndexError:
    print('Uruchomienie programu: python zad_5_1_a.py zawodnicy.csv')
    exit(1)

except FileNotFoundError:
    print(f'Plik {nazwa_pliku} nie odnaleziony!')
    exit(1)






