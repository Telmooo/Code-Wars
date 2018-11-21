def binary_pyramid(m,n):
    return str(binary(sum(binary(x) for x in range(m, n+1))))

def binary(x):
    binary = ""
    while x:
        binary = ("1" if x%2 else "0") + binary
        x //= 2
    return int(binary) if binary else 0
