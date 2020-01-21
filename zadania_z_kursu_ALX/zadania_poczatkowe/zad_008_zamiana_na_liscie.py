"""
Napisz program zamieniający miejscami w zadanej liście liczb
element największy z najmniejszym.
"""


def zamiana(lista_liczb):

    if lista_liczb == []:
        raise ValueError('Pusta lista.')

    for element in lista_liczb:
        if not (type(element) == int or type(element) == float):
            raise TypeError('Nieprawidłowy typ elementu listy.')


    indeks_min = None
    indeks_max = None

    for indeks, wartosc in enumerate(lista_liczb):
        if indeks_min is None or wartosc < lista_liczb[indeks_min]:
            indeks_min = indeks
        if indeks_max is None or wartosc > lista_liczb[indeks_max]:
            indeks_max = indeks

    # print("indeks min", indeks_min)
    # print("indeks max", indeks_max)

    lista_liczb[indeks_max], lista_liczb[indeks_min] = lista_liczb[indeks_min], lista_liczb[indeks_max]
    # print(lista_liczb)

    return lista_liczb

import pytest

def test_zamiana1():
    assert zamiana([3, 4, 1]) == [3, 1, 4]

def test_zamiana2():
    assert zamiana([0.1,3,-1000,-1001,45,2,2]) == [0.1,3,-1000,45,-1001,2,2]

def test_zamiana3():
    with pytest.raises(ValueError):
        zamiana([])

def test_zamiana4():
    with pytest.raises(TypeError):
        zamiana([0.2,3,4,'abcd',3])
