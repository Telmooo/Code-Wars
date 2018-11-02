def persistence(n):
    steps = 0
    num = n
    while num >= 10:
        pivot = 1
        size = len(str(num))
        for i in range(size):
            pivot *= (num%10)
            num //= 10
        num = pivot
        steps += 1
    return steps
