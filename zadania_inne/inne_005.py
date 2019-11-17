# Napisz program, który na podstawie listy utworzy dwie nowe listy
# - jedną z elementami nieujemnymi oraz drugą z elementami ujemnymi.

lista_wszystkich = [1, 5, 10, -1, 2, -3, 0, 8, 100, -3, -9, -1000 -21313, 4, 5, 3]

lista_nieujemnych = [ element for element in lista_wszystkich if element >= 0 ]
lista_ujemnych = [ element for element in lista_wszystkich if element < 0 ]

print(lista_nieujemnych)
print(lista_ujemnych)

#
# lista_polaczona = list(zip(lista_nieujemnych,lista_ujemnych))
# print(lista_polaczona)
