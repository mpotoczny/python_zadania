def zamiana(lista_liczb):

    if lista_liczb == []:
        raise ValueError('Pusta lista.')

    for element in lista_liczb:
        if not ( type(element) == int or type(element) == float ):
            raise TypeError("Nieprawidłowy typ elementu.")

    indeks_min = None
    indeks_max = None

    for indeks, wartosc in enumerate(lista_liczb):
        if indeks_min is None or wartosc < lista_liczb[indeks_min]:
            indeks_min = indeks
        if indeks_max is None or wartosc > lista_liczb[indeks_max]:
            indeks_max = indeks

    lista_liczb[indeks_max], lista_liczb[indeks_min] = lista_liczb[indeks_min], lista_liczb[indeks_max]
    return lista_liczb

example_list = [-9,-11,3,7,1]
print(example_list)
a = zamiana(example_list)
print(a)