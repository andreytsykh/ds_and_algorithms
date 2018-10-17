def eratosthenes_sieve(n):
    primes = [True for p in range(n+1)]
    p = 2

    while(p**2 < n):
        if primes[p] == True:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1

    return primes

if __name__ == '__main__':
    for i, p in enumerate(eratosthenes_sieve(30)):
        if p:
            print(i, end = ' ')