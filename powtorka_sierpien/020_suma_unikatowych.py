# def unique_sum(lst):
    # # sposób 1
    # if lst == []:
    #     return None
    #
    # elements = set()
    # for x in lst:
    #     elements.add(x)
    # return sum(elements)

# # SPOSÓB 2
unique_sum = lambda l: sum(set(l)) if l else None

a = unique_sum([1,2,3])
print(a)
a = unique_sum([1,3,8,1,8])
print(a)
a = unique_sum([-1,-1,5,2,-7])
print(a)
a = unique_sum([])
print(a)