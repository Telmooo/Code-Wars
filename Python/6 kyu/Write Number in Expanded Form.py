def expanded_form(num):
    r = []
    for i, n in zip(range(len(str(num))-1, -1, -1), str(num)):
        if n != "0":
            r.append(f"{int(n)*(10**i)}")
    return " + ".join(r)
