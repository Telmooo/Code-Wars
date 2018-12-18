def mygcd(n1, n2):
    if n1==0 or n2==0:
        return
    x = n1%n2
    if x:
        return mygcd(n2, x)
    return n2
