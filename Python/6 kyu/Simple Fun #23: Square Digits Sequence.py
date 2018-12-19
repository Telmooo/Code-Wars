def square_digits_sequence(n):
    from functools import reduce
    deposit = set()
    while n not in deposit:
        deposit.add(n)
        n = reduce(lambda x, y: x+y, map(lambda x: int(x)**2, str(n)))
    return len(deposit)+1
