def num_primorial(n):
    from functools import reduce
    return reduce(lambda x, y: x*y, get_primes(n))

def get_primes(n):
    primes = []
    p = 2
    while len(primes) != n:
        if p == 2: primes.append(p); p += 1; continue

        is_prime = True
        for i in range(2, p):
            if p%i == 0: is_prime = False; break

        if is_prime: primes.append(p);
        p += 1
    return primes
