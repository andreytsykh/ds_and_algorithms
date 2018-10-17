def eratosthenes_sieve(n):
    primes = [True for p in range(n+1)]
    p = 2

    while(p**2 < n):
        if primes[p] == True:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1

    return primes

def eratosthenes_generator(n):
    primes = [True] * n
    primes[0] = primes[1] = False

    for i, isprime in enumerate(primes):
        if isprime:
            yield i
            for n in range(i*i, n, i):
                primes[n] = False

def print_primes(n):
    yield from eratosthenes_generator(n)


if __name__ == '__main__':
    for i, p in enumerate(eratosthenes_sieve(30)):
        if p:
            print(i, end = ' ')
    print('\n')
        
    for i in print_primes(30):
        print(i, end=' ')
    
   