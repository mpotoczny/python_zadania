def nearest_fibonacci(number):

    # # 0 sposób - za wolny
    # a, b = 0, 1
    # fibo_list = [a]
    # for _ in range(number+1):
    #     a, b = b, a + b
    #     fibo_list.append(a)
    #
    # diffs = [ abs(number - elem) for elem in fibo_list ]
    # value = min(diffs)
    # ind = diffs.index(value)
    # return fibo_list[ind]
    #
    # # 1 SPOSÓB
    # a, b = 1, 2
    # for _ in range(number):
    #     if a <= number < b: # inaczej -> if number in range(a, b):
    #         if abs(number - a) > abs(number - b):
    #             return b
    #         else:
    #             return a
    #     a, b = b, a + b
    #
    # # 2 SPOSÓB
    # a, b = 1, 2
    # for _ in range(number):
    #     if a <= number < b:
    #         return b if abs(number - a) > abs(number - b) else a
    #     a, b = b, a + b
    #
    # # 3 SPOSÓB
    # a, b = 1, 2
    # while(1):
    #     f = lambda a, b, number: b if abs(number-a) > abs(number-b) else a
    #     if a <= number < b:
    #         return f(a,b,number)
    #     a,b = b, a + b
    #
    #
    # # 4 SPOSÓB
    a, b = 1, 2
    for _ in range(number):
        if a <= number < b:
            dictionary1 = {a: abs(number-a), b: abs(number-b)}
            return min(dictionary1, key=dictionary1.get)
        a, b = b, a + b




print( nearest_fibonacci(1) )
print( nearest_fibonacci(2) )
print( nearest_fibonacci(9) )
print( nearest_fibonacci(17) )
print( nearest_fibonacci(54) )

# nearest_fibonacci(1)
# nearest_fibonacci(2)
# nearest_fibonacci(9)
# nearest_fibonacci(17)
# nearest_fibonacci(54)