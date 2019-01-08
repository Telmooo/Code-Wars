def mix(s1, s2):
    d = {}

    for char in set(s1):
        if char.islower():
            occ = s1.count(char)
            if occ > 1:
                d[char] = (occ, "1")

    for char in set(s2):
        if char.islower():
            occ = s2.count(char)
            if occ > 1:
                stored = d.get(char, (0, None))[0]
                if occ > stored:
                    d[char] = (occ, "2")
                elif occ == stored:
                    d[char] = (occ, "=")

    l = sorted(d.items(), key = lambda x: (-x[1][0], x[1][1], x[0]))
    
    return "/".join(f"{i[1][1]}:{i[0]*i[1][0]}" for i in l)
