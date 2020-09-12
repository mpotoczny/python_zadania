# DEKORATORY
print()
# funkcje w funkcji

def przedstaw_dzieciaki():
    def pierwsze_dziecko():
        print("Ala")

    def drugie_dziecko():
        print("Piotr")

    pierwsze_dziecko()
    drugie_dziecko()

przedstaw_dzieciaki()

# zasieg zmiennych
print()

def a(x):
    def b():
        print(x)

    b()

a(5)

print('\ndekoratorki $$$$$$$$$$$$$$ \n')
def dekorator(x):
    def opakowywacz():
        print(x)

    return opakowywacz

funkcja_z_srodka = dekorator(10)

print(1)
funkcja_z_srodka()
print(2)
funkcja_z_srodka()

funkcja2 = dekorator(30)
funkcja2()

def hello_world():
    return "hello world!"

opakowana = dekorator(hello_world()) # OPAKOWUJE WYWOLANIE FUNKCJI
opakowana = dekorator(hello_world) # OPAKOWUJE OBIEKT FUNKCJI
opakowana()



def powiedz_czesc(imie):
    return f'Czesc {imie}!'

def powiedz_jestes_super(imie):
    return f'{imie}, jesteś super!!!'

def pozdrow_piotrka(funkcja_do_pozdrawiania, imie):
    return funkcja_do_pozdrawiania(imie)


print( pozdrow_piotrka(powiedz_czesc, 'Piotr') )
print( pozdrow_piotrka(powiedz_jestes_super, 'Ala') )


def przedstaw_dzieciaki(ktore):
    def pierwsze_dziecko():
        print("Ala")

    def drugie_dziecko():
        print("Piotr")

    if ktore == 1:
        pierwsze_dziecko()
    else:
        drugie_dziecko()

przedstaw_dzieciaki(1)
przedstaw_dzieciaki(2)
print()


def przedstaw_dzieciaki(ktore):
    def pierwsze_dziecko():
        print("Ala")

    def drugie_dziecko():
        print("Piotr")

    if ktore == 1:
        return pierwsze_dziecko
    else:
        return drugie_dziecko

funkcja_dziecko = przedstaw_dzieciaki(2)
funkcja_dziecko()
print()
przedstaw_dzieciaki(1)()

def funkcja(*args, **kwargs):
    print(args, kwargs)

funkcja(1,2,3, a=1,b=2,c=3)


# no to teraz już na prawde dekoratory :D
def dekorator(funkcja_do_udekorowania):
    def opakowanie(*args, **kwargs):
        print('Przed wywołaniem')
        wynik = funkcja_do_udekorowania(*args, **kwargs)
        print('Po wywołaniu')
        return wynik

    return opakowanie

def hello_world():
    print('Hello world!')

hello_world()


udekorowane_hello_world = dekorator(hello_world)
udekorowane_hello_world()


udekorowane_print = dekorator(print)
udekorowane_print('Ala', 1, 3, True, None)


udekorowane_sum = dekorator(sum)
print( udekorowane_sum([10,20,30]) )

@dekorator
def sumator(a, b):
    return a+b

def sumator1(a, b):
    return a+b

sumator_udekorowany1 = dekorator(sumator1)

suma = sumator(5, 3)
print(suma)


# domknięcie / closure
def stworz_przemnazacz(x):
    def przemnazacz(y):
        return x*y

    return przemnazacz


przez_5 = stworz_przemnazacz(5)

print( przez_5(10) )






