def flatten_and_sort(array):

    # # 1 sposób - alx
    # flattened, ordered = list(), list()
    # for elem in array:
    #     if type(elem) == list:
    #         flattened += flatten_and_sort(elem)
    #     else:
    #         flattened.append(elem)
    #     ordered = sorted(flattened)
    # return ordered

    # # 2 sposób - stackoverflow
    # flattened = [item for sublist in array for item in sublist]
    # ordered = sorted(flattened)
    # return ordered

    # 3 sposób - stackoverflow
    flattened = sorted(sum(array, []))
    ordered = sorted(flattened)
    return ordered

res1 = flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])
print(res1)
