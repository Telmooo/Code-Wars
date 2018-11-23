def dig_pow(n, p):
    x = sum(pow(int(d), idx+p) for idx, d in enumerate(str(n)))
    return -1 if x%n else x//n
