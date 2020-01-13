def stopy_na_metry(stopy: float) -> float:
    """
    Funkcja przelicza stopy na metry
    :param stopy:
    :return:
    """
    stopy = float(stopy)
    metry = stopy * 0.3048
    return round(metry, 2)

def max(a:int, b:int):
    if a > b:
        maxval = a
    else:
        maxval = b

    return maxval

def bmi(wzrost: int, masa: float):
    wspolczynnik = round( float(masa / ((wzrost/100) ** 2)), 2 )

    opinia = None

    if wspolczynnik < 18.5:
        opinia = "niedowaga"
    elif wspolczynnik >= 18.5 and wspolczynnik < 24.99:
        opinia = "waga normalna"
    elif wspolczynnik >= 25 and wspolczynnik < 29.99:
        opinia = "nadwaga"
    elif wspolczynnik >= 30 and wspolczynnik < 34.99:
        opinia = "otylosc 1 stopnia"
    elif wspolczynnik >= 35 and wspolczynnik < 39.99:
        opinia = "otylosc 2 stopnia"
    else:
        opinia = "otylosc 3 stopnia"

    return wspolczynnik, opinia



print(stopy_na_metry(139.33))
print(max(-6,9))
print(bmi(165,71.2))

