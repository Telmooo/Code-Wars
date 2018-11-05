def nb_dig(n, d):
    return "".join(str(k ** 2) for k in range(n+1)).count(str(d))
