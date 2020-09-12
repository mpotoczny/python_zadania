#    Wypisz wszystkie liczby od 1 do 100
#   Jeśli liczba jest podzielna przez trzy wypisz “Fizz“
#    Jeśli liczba jest podzielna przez pięć wypisz “Buzz“
#    Jeśli liczba jest podzielna przez trzy i pięć wypisz “FizzBuzz“

for liczba in range(1, 101):

    trojka = True if liczba % 3 == 0 else False
    piatka = True if liczba % 5 == 0 else False

    if trojka is True and piatka is True:
        print("FizzBuzz")
    elif trojka is True:
        print('Fizz')
    elif piatka is True:
        print("Buzz")
    else:
        print(liczba)
