# SPOSÓB 2
def SumEvenFibonacci2(limit):

    start = time.time()

    sum = 0
    fibonacci_list = [0,1]
    for i in range(1, limit+1):
        x = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(x)
        if x % 2 == 0 and x <= limit:
            sum += x
    # print(fibonacci_list)
    print(sum)

    stop = time.time()
    interval = stop - start
    print(f'Czas trwania funkcji - {interval:.2f} s')

    return sum

#############################
def SumEvenFibonacci(limit):
    sum = 0
    a = 0
    b = 1
    for i in range(1, limit + 1):
        c = a + b
        a = b
        b = c

        if c % 2 == 0 and c <= limit:
            sum += c

    return sum

