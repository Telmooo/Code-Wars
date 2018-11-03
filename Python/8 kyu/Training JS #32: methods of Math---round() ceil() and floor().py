from math import ceil, floor

def round_it(n):
    l = str(n).split(".")
    return ceil(n) if len(l[1]) > len(l[0]) else floor(n) if len(l[0]) > len(l[1]) else round(n)
