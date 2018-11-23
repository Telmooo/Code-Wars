def clean_string(s):
    delete = 0
    l = []
    for c in s:
        if c == "#": delete += 1
        else: l.append(c)
        if delete != 0:
            l = l[:-delete]
            delete = 0
    return "".join(l)
