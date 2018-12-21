def solve(s):
    c = set(s)
    count = {}
    for char in c:
        count[char] = s.count(char)
    for c1 in c:
        x = count[c1]-1
        equal = True
        if x>0:
            for c2 in c-{c1}:
                if x != count[c2]: equal = False; break
            if equal: return True
        else:
            t = -1
            for c2 in c-{c1}:
                if t==-1: t = count[c2]; continue
                
                if t != count[c2]: equal = False; break
            if equal: return True
    return False
