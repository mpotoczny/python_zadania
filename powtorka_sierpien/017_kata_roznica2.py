def twos_difference(lst):
    result = []
    for elem in lst:
        if elem+2 in lst:
            result.append((elem, elem+2))

    result.sort()
    # # lub
    # result.sort(key=lambda x: x)

    return result

x = twos_difference([6,3,4,1,5])
print(x)