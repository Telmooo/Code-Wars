def parse(data):
    i = 0
    r = []
    for x in data:
        if x == "o":
            r.append(i)
        if x == "d":
            i -= 1
        if x == "i":
            i += 1
        if x == "s":
            i **= 2
    return r
