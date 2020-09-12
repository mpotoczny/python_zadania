dancing_brigade = 'CbcBcbaA'
print(dancing_brigade)
print(type(dancing_brigade))
print("**************")
# print( dancing_brigade.sort() ) # -> blad


# napis = input("Podaj napis: ")
# print(napis)
# print(type(napis))
# print("**************")
print('a'*30)

lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)
print('a'*30)

lst = ['abb', 'ABB', 'aBa', 'AbA']
y = sorted(lst, key=lambda L: (L.lower(), L))
print(y)
print('a'*30)

for i in range(10):
    print(i, end=" ")
print('a'*30)

txt = str()
txt = ""
print(type(txt))
print('a'*30)

from collections import defaultdict
info = defaultdict(int) # wartość domyślna, intowe 0

info['wiek'] += 10
print(info)

slownik = defaultdict(str)
print(f" >>{slownik['a']}<< ")

# fabryki wartości domyślnych: int, str, float, tuple, list, set, dict

slownik = defaultdict(list)
print(slownik['a'])

slownik = defaultdict(dict)
print(slownik['a'])
print('a'*30)

a = [10,20,30,40]
b = ['be', 'me', 'ce', 'de']
c =  list( a[3:] + a + a + b + lst[1:2])[:10] # ostatni nawias i liczba określa ilość elementów
print(c)
print('a'*30)

c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))

print( chr(65) )
chr(65)

myList = [list(range(ord('a'),ord('z')))]
print(myList)
print('a'*30,'\n')

txt = 'nabx'
print(f'dlugosc tekstu to {len(txt)}')
print( range(len(txt) ) )

for i in range(len(txt) ):
    print(i)
    print( ord( txt[i] ))

print('a'*30,'\n')

x = 'a' < 'b'
print(x)

print()
def nothing():
    print("nic")

print(nothing)
print('a'*30,'\n')

rates = {
    1: 40,
    2: 100,
    3: 300,
    4: 1200
}

tabo = [1,2,3,4]
for x in tabo:
    print( rates[x] )

print('\n','CIĄG FIBONACCIEGO')
fibonacci_list = [0,1]
limit = 10
for i in range(2, limit+1):
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

print(fibonacci_list)

print('a'*30,'\n')
from math import sqrt
def fibo(n):
    x = ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
    print(x)
fibo(34)

print('a'*30,'\n')

def SumEvenFibonacci(limit):
    a = 1
    b = 2
    sum = 0
    while a < limit:
        a, b = b, a + b
        if a % 2 == 0:
            sum += a
    return sum

print('a'*30,'\n')
import random
def scramble(word):
    if len(word) <= 2: return word
    return word[0] + "".join(sorted(word[1:-1], key=lambda x: random.random())) + word[-1]
print(scramble('dusdasdsaza'))

print('a'*30)
myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)

print('a'*30,'\n')
a = [0,1,2]
x = a[-1:-1]+["abecadlo"]
print(x)

print('a'*30,'\n')
txt = 'skoczek'
modified = txt + '1'
print(modified)

print('a'*30,'\n')
x = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), 'AGENT', (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)]
print(x[0][1])

print('a'*30,'\n')
tupelka = (11,12,13,14)
print(tupelka[2])

print()
print()

a = {'a': 3, 'b': 2, 'c': 6}
b = {'b': 7, 'c': 4, 'd': 1}
c = {'c': 1, 'd': 5, 'e': 7}

all_dicts = [a,b,c]

from functools import reduce

all_keys = reduce((lambda x,y : x | y),[d.keys() for d in all_dicts])

max_dict = { k : max(d.get(k,0) for d in all_dicts) for k in all_keys }
print(max_dict)