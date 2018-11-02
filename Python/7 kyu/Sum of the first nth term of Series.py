def series_sum(n):
    sum_ = 0
    for i in range(n):
        sum_ += 1 / (1 + 3*i)
    return "%.2f" % sum_
