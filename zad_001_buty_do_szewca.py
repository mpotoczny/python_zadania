#  Zadanie 2.2 | Buty do szewca
#
# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
# (poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.

numer_dnia_oddania = None

while True:

    dzien_oddania = input("W jaki dzien tygodnia oddales buty do szewca? ")

    if dzien_oddania.upper() == "PONIEDZIALEK":
        numer_dnia_oddania = 1
    elif dzien_oddania.upper() == "WTOREK":
        numer_dnia_oddania = 2
    elif dzien_oddania.upper() == "SRODA":
        numer_dnia_oddania = 3
    elif dzien_oddania.upper() == "CZWARTEK":
        numer_dnia_oddania = 4
    elif dzien_oddania.upper() == "PIATEK":
        numer_dnia_oddania = 5
    elif dzien_oddania.upper() == "SOBOTA":
        numer_dnia_oddania = 6
    elif dzien_oddania.upper() == "NIEDZIELA":
        numer_dnia_oddania = 7
    else:
        print("Nie ma takiego dnia! Jeszcze raz!")
        continue


    ilosc_dni_naprawy = int(input("Ile dni będzie trwała naprawa? "))

    numer_dnia_odebrania = numer_dnia_oddania + ilosc_dni_naprawy

    if numer_dnia_odebrania % 7 == 0:
        print("Buty odbierzesz w niedzielę!")
    elif numer_dnia_odebrania % 7 == 1:
        print("Buty odbierzesz w poniedziałek!")
    elif numer_dnia_odebrania % 7 == 2:
        print("Buty odbierzesz we wtorek")
    elif numer_dnia_odebrania % 7 == 3:
        print("Buty odbierzesz w środę!")
    elif numer_dnia_odebrania % 7 == 4:
        print("Buty odbierzesz w czwartek!")
    elif numer_dnia_odebrania % 7 == 5:
        print("Buty odbierzesz w piątek!")
    elif numer_dnia_odebrania % 7 == 6:
        print("Buty odbierzesz w sobotę!")
    break
