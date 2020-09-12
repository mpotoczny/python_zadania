'''
Legend:
-Uppercase letters stands for mothers, lowercase stand for their children,
i.e. "A" mother's children are "aaaa".
-Function input: String contains only letters, uppercase letters are unique.
Task:
Place all people in alphabetical order where Mothers are followed
by their children, i.e. "aAbaBb" => "AaaBbb".
'''


dancing_brigade = "FfUuuuXx"
print(dancing_brigade)

wystapienia = {}
for znak in dancing_brigade:
    if znak not in wystapienia:
        wystapienia[znak] = 0
    wystapienia[znak] += 1

print(sorted(wystapienia.items()))
print("**************")
# for litera in sorted(wystapienia, key=str): # dostajemy listę kluczy ze słownika
#     print(f'{litera} - {wystapienia[litera]}')

# for litera in wystapienia:
#     print(f'{litera}*{wystapienia[litera]}')

print("\n************** SPOSÓB 1")
wynik = str()
for litera, liczba_wystapien in sorted(wystapienia.items()): # sorted sortuje tu najpierw wszystkie wielkie litery, a później wszystkie małe
    if litera.isupper(): # sortowanie wykonuje się tylko jeśli jest wielka litera, bez niej małe pomijam
        if litera.lower() in wystapienia.keys(): # sprawdzenie czy są małe i dodanie do stringa
            txt = f'{litera}'*liczba_wystapien + f'{litera.lower()}'*wystapienia[litera.lower()]
            wynik += txt
        else: # jeśli małych liter brak wypisanie tylko wielkich
            txt = f'{litera}'*liczba_wystapien
            wynik += txt
print(wynik)


print("\n************** SPOSÓB 2")
lista = sorted(dancing_brigade, key=lambda x: (x.lower(), x)) # tworzy listę
wynik_string = "".join(lista) # przerabia na stringa
print(wynik_string)




# Test.describe("Basic tests")
# Test.assert_equals(find_children("abBA"), "AaBb")
# Test.assert_equals(find_children("AaaaaZazzz"), "AaaaaaZzzz")
# Test.assert_equals(find_children("CbcBcbaA"), "AaBbbCcc")
# Test.assert_equals(find_children("xXfuUuuF"), "FfUuuuXx")
# Test.assert_equals(find_children(""), "")