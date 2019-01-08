def mix(s1, s2):
    compare = lambda x, y: 0 if x > y else 1 if x < y else 2
    l = []
    for c in set(s1+s2):
        if c.islower():
            occ1, occ2 = s1.count(c), s2.count(c)
            if occ1 > 1 or occ2 > 1:
                l.append(f"{'12='[compare(occ1, occ2)]}:{c*max(occ1, occ2)}")
    return "/".join(sorted(l, key = lambda x: (-len(x), x)))
