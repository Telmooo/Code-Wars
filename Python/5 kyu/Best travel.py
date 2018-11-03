from itertools import combinations

def choose_best_sum(t, k, ls):
        return max([sum(combination) for combination in combinations(ls, k) if sum(combination) <= t], default = None)
