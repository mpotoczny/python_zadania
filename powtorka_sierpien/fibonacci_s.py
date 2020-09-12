# efficient
# zwraca n-ty wyraz ciągu fibonacciego
def fn_fibonacci(number):
    a, b = 0, 1
    for _ in range(number):
        a, b = b, a + b
    print(a)
    return a


# with list
def fibo_list(limit):
    #poprawna lista do n-tego wyraz ciągu fibonacciego
    a, b = 0, 1
    fibo_list = [a]
    for _ in range(limit):
        a, b = b, a + b
        fibo_list.append(a)
    print(fibo_list)
    return fibo_list

    #niepoprawna lista dla zerowego ciagu n-tego wyraz ciągu fibonacciego, poza tym ok
    # fibonacci_list = [0,1]
    # for i in range(1, limit):
    #     fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    # print(fibonacci_list)
    # # return fibonacci_list

# fn_fibonacci(0)
# fn_fibonacci(1)
# fn_fibonacci(2)
# fn_fibonacci(3)
# fn_fibonacci(10)

fibo_list(0)
fibo_list(1)
fibo_list(2)
fibo_list(3)
fibo_list(4)