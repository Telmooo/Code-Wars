def solve(st, idx):
    if st and st[idx] == "(":
        control = 1
        for i, c in enumerate(st[idx+1:]):
            if c == "(": control += 1
            if c == ")": control -= 1
            if control == 0: return i+idx+1
    return -1
