def count_positives_sum_negatives(arr):
    return [len([digit for digit in arr if digit > 0]), sum([digit for digit in arr if digit < 0])] if arr else []
