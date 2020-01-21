# lista = [ [2,2], [3,4], [4,1], [1,3] ]
# print(lista)
# lista.sort(key=lambda x: x[1] )
# print(lista)


# from collections import Counter
# co = Counter(epos_text)
# print(co)
#
# ilosc = sum(co.values())
# print(ilosc)


# text = 'ABC..;;; dsa;;; /n ds;;sa ... !!fdsfds dSFDfbec!adlopo222!122 ?? ;; s;s; a;b;c!'
# print(text)
# characters = '.,;\\n\?!'
# for c in text:
#     if c in characters:
#         text = text.replace(c, " ")
#
#
# print(text)

a = int(False)
b = int (not a)
print(a, b)

def zamien(j):
    if j == 0:
        j = 1
    elif j == 1:
        j = 0
    return j

print(zamien(0))
print(zamien(1))

print('*' * 6)
print( 1 == True )
print('*' * 6)

a = 5

print( type(int) )