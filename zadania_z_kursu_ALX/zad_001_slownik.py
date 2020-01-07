DNI_TYGODNIA = {
    "PONIEDZIAŁEK": 1,
    "WTOREK": 2,
    "ŚRODA": 3,
    "CZWARTEK": 4,
    "PIĄTEK": 5,
    "SOBOTA": 6,
    "NIEDZIELA": 0,
}

dzien_oddania = input("W jaki dzien tygodnia oddales buty do szewca? ")
dzien_oddania = dzien_oddania.upper()

if dzien_oddania in DNI_TYGODNIA.keys():
    numer_dnia_oddania = DNI_TYGODNIA.get(dzien_oddania)
else:
    raise ValueError("Podałeś coś, co nie jest dniem tygodnia.")


ilosc_dni_naprawy = int(input("Ile dni będzie trwała naprawa? "))
numer_dnia_odebrania = numer_dnia_oddania + ilosc_dni_naprawy

x = numer_dnia_odebrania % 7
for nazwa, numer in DNI_TYGODNIA.items():
    if x == numer:
        print(f"Buty odbierzesz następującego dnia: {nazwa}")

