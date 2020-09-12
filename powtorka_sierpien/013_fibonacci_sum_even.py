'''
Sum Even Fibonacci Numbers

 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
sumEvenFibonacci(8) // returns 10 by adding the even values 2 and 8
'''
import time

# SPOSÓB 1 - z listą -> obciąża pamięć
def SumEvenFibonacci(limit): # parzyste

    start = time.time()
    fibonacci_list = [0,1]
    for i in range(1, limit+1):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    # print(fibonacci_list)

    sum = 0
    for factor in fibonacci_list:
        if factor % 2 == 0 and factor <= limit:
            # print(f'to ten - {factor}')
            sum += factor

    stop = time.time()
    interval = stop - start
    print(f'Czas trwania funkcji - {interval:.2f} s')
    return sum


# SPOSÓB 2 - szybki
def SumEvenFibonacci2(limit):

    start = time.time()

    a = 0
    b = 1
    sum = 0
    while a < limit:
        a, b = b, a + b
        if a % 2 == 0:
            sum += a

    stop = time.time()
    interval = stop - start
    print(f'Czas trwania funkcji - {interval:.2f} s')

    return sum

print("-"*30)
# print(f"dla 0 to { SumEvenFibonacci(0) }")
# print(f"dla 1 to { SumEvenFibonacci(1) }")
# print(f"dla 2 to { SumEvenFibonacci(2) } \n")
# print(f"dla 8 to { SumEvenFibonacci(8) } \n")
# print(f"dla 111111 to { SumEvenFibonacci(111111) } \n")

print("-"*30)

print(f"dla 0 to { SumEvenFibonacci2(0) }")
print(f"dla 1 to { SumEvenFibonacci2(1) }")
print(f"dla 2 to { SumEvenFibonacci2(2) } \n")
print(f"dla 8 to { SumEvenFibonacci2(8) } \n")
print(f"dla 111111 to { SumEvenFibonacci2(111111) } \n")
print(f"dla 33 to { SumEvenFibonacci2(33) } \n")
print(f"dla 25997544 to { SumEvenFibonacci2(25997544) } \n")
print(f"dla 979802529  to { SumEvenFibonacci2(979802529) } \n")
