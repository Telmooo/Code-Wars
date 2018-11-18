def collatz(n):
    l = 1
    x = n
    while x != 1:
        x = x*3+1 if x%2 else x//2
        l += 1
    return l
