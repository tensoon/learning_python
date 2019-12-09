from functools import lru_cache

"""fib_cache = {}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value =1
    elif n > 2:
        value = fib(n-1) + fib(n-2)
    fib_cache[n] = value
    return value

for n in range(1, 10000):
    print(f"{n} : {fib(n)}")"""

@lru_cache(maxsize=100000)
def fib2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib2(n-1) + fib2(n-2)

for n in range(1, 501):
    print(f"{n} : {fib2(n)}")