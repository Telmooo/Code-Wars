def distinct(seq):
    ls = []
    for n in seq:
        if n not in ls:
            ls.append(n)
    return ls
