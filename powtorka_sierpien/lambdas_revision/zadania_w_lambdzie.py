# suma unikatowych liczb na liście
lista1 = (1,2,4,1,2,3,5,4,9,7,8,8,7)
lista2 = []
unique_sum = lambda lista: sum(set((lista))) if lista != [] else None

print( unique_sum(lista1) )
print(unique_sum(lista2))

print('-' * 40)
# # splaszczenie listy
# lista = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
# flatten_and_sort = lambda a, b=[]: b.clear() or list(map(b.extend, a)) and sorted(b)
# print( flatten_and_sort(lista) )

print('-' * 40)
# pary liczb - roznica 2
lista3 = (1,2,4,1,2,3,5,4,9,7,8,8,7)
twos_difference = lambda lst: [(i, i+2) for i in sorted(lst) if i+2 in lst]
print(twos_difference(lista3))

print('-' * 40)
# suma liczb podzielnych przez 3 i 5 poniżej zadanej
n = 10
solution1 = lambda elem: sum(k for k in range(n) if k % 3 == 0 or k % 5 == 0)
print(solution1(n))

print('-' * 40)
# najbliższy fibonacci
def nearest_fibonacci(number):
    # a, b = 1, 2
    # while(1):
    #     if a <= number < b: # inaczej -> if number in range(a, b):
    #         if abs(number - a) > abs(number - b):
    #             return b
    #         else:
    #             return a
    #     a, b = b, a + b

    a, b = 1, 2
    f = lambda a, b, number: b if abs(number-a) > abs(number-b) else a
    if a <= number < b:
        return f(a,b,number)
    a,b = b, a + b



print(nearest_fibonacci(11))
