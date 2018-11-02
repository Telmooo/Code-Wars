import numpy as np

def iq_test(numbers):
    numbers_ = np.array(numbers.split(), dtype = int)
    values = (numbers_ % 2) == 0
    value, count = np.unique(values, return_counts = True)
    counter = dict(zip(value, count))
    if counter.get(False) > counter.get(True):
        return values.tolist().index(True) + 1
    return values.tolist().index(False) + 1
