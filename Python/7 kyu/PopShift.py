def pop_shift(str):
    sol0 = ""
    sol1 = ""
    while len(str) > 1:
        sol0 += str[-1]
        sol1 += str[0]
        str = str[1:-1]
    return [sol0, sol1, str]
