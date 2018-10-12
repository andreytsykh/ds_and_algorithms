
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


print(fib(200))


