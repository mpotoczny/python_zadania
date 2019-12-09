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
