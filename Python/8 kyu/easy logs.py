def logs(x, a, b):
    ln_ab = sum(((1 / (2 * n + 1)) * (((a * b - 1)/(a * b + 1)) ** (2 * n + 1))) for n in range(900000))
    ln_x = sum(((1 / (2 * n + 1)) * (((x - 1) / (x + 1)) ** (2 * n + 1))) for n in range(900000))
    return (ln_ab / ln_x)
