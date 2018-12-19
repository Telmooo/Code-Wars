def revrot(strng, sz):
    if not strng or sz<=0 or sz > len(strng): return ""
    chunks = []
    while len(strng) >= sz:
        t = strng[:sz]
        if len(t)>=sz: chunks.append(t)
        strng = strng[sz:]
    st = ""
    for c in chunks:
        s = sum(list(map(lambda x: int(x)**3, c)))%2==0
        if s:
            st += c[::-1]
        else: st +=  c[1:] + c[0]
    return st
