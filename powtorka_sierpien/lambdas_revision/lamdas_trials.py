fun1 = (lambda x: x+1)
print(fun1(9))
print('-'*30)

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print( full_name('guido', 'van rossum') )
print('-'*30)
# div_zero = lambda x: x / 0
# div_zero(6)

# def div_zero_n(x): return x / 0
# div_zero_n(10)

e = lambda x: x % 2 and 'nieparzysty' or 'parzysty'
print( e(3) )

f = lambda x: x == 15 and 'tak' or 'nie' # po AND zwraca jesli true; po OR zwraca jesli false
print( f(150) )

print('-'*30)
lista = [4,5,6]
e1 = lambda z: z+3
zwiekszony = e1(lista[2])
print(zwiekszony)