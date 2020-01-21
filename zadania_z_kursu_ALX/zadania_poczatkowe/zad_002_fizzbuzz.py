#    Wypisz wszystkie liczby od 1 do 100
#   Jeśli liczba jest podzielna przez trzy wypisz “Fizz“
#    Jeśli liczba jest podzielna przez pięć wypisz “Buzz“
#    Jeśli liczba jest podzielna przez trzy i pięć wypisz “FizzBuzz“


trojka = None
piatka = None

for x in range(1, 101):

    if x % 3 == 0:
        trojka = True
    else:
        trojka = False

    if x % 5 == 0:
        piatka = True
    else:
        piatka = False

    if ((trojka == True) and (piatka == True)):
        print("FizzBuzz")
    elif (trojka == True):
        print("Fizz")
    elif (piatka == True):
        print("Buzz")
    else:
        print(x)

    trojka = False
    piatka = False