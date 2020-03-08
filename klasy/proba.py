a = "napisnapis"
print(a)
print("=" * len(a))
print()
print(f"{a}\n{'='*len(a)} ")

print("*"*50,end='\n\n')

tekst = 'Onet'
link = 'onet.pl'
print( f"({tekst})[http://{link}]" )
print("*"*50,end='\n\n')

class Ludzie:
    pass

l1 = Ludzie()
l2 = Ludzie()

lista = []
print(lista)
lista.append(l1)
lista.append(l2)
print(lista)
print("*"*50,end='\n')

#jeżeli lista jest niepusta to bool(lista) zwraca True
b1 = [3,2,'january',2009]
stan = bool(b1)
print(stan)

#jeżeli lista nie ma elementów to bool(lista) zwraca False
b1.clear()
stan = bool(b1)
print(stan)

print("*"*50,end='\n')
b1 = [3, 2, 12, 2009]
a = min(b1)
print(a)
