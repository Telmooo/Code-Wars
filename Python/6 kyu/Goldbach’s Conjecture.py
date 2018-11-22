def goldbach_partitions(n):
    partitions = []
    known = {2: 0}
    if n%2==0:
        if is_prime(n-2, known):
            partitions.append(f"2+{n-2}")
            known[n-2] = 0
        for i in range(3, n//2+1, 2):
            if is_prime(i, known) and is_prime(n-i, known):
                known[i], known[n-i] = 0, 0
                partitions.append(f"{i}+{n-i}")
    return partitions

def is_prime(n, known={}):
    if n<2: return False
    elif n in known: return True
    i = 2
    while i**2 <= n:
        if n%i==0:
            return False
        i+=1
    return True
