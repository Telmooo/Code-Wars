def count_sheep(n):
    return "".join("{} sheep...".format(x+1) for x in range(n))
