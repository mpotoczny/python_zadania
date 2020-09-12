def fizzBuzz(n):
    a = lambda x: str(x)
    b = lambda x: 'Fizz'
    c = lambda x: 'Buzz'
    d = lambda x: 'FizzBuzz'
    nums = [d, a, a, b, a, c, b, a, a, b, c, a, b, a, a]
    return [nums[i % 15](i) for i in range(1, n + 1)]

rezultat = fizzBuzz(33)
print(rezultat)