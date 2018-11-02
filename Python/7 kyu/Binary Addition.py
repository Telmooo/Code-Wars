#Add integers then convert to binary
def add_binary(a,b):
    sum_ = a + b
    i = 0
    binary = 0
    while sum_ > 0:
        binary += (sum_ % 2) * (10**i)
        sum_ >>= 1
        i += 1
    return str(binary)

#Convert to binary and sum the numbers in binary
def add_binary(a,b):
    x = ""
    y = ""
    while a > 0:
        x = str((a % 2)) + x
        a >>= 1

    while b > 0:
        y = str((b % 2)) + y
        b >>= 1

    bits = max(len(x), len(y))
    x = x.zfill(bits)
    y = y.zfill(bits)
    result = ""
    carry = 0

    for i in range(bits -1, -1, -1):
        k = carry
        k += 1 if x[i] == "1" else 0
        k += 1 if y[i] == "1" else 0
        result = ("1" if k % 2 == 1 else "0") + result
        carry = 0 if k < 2 else 1

    if carry != 0: result = "1" + result

    return result
