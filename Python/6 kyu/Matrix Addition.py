def matrix_addition(a, b):
    matrix_sum = []
    for i in range(len(a)):
        matrix_sum.append([a[i][j]+b[i][j] for j in range(len(a[0]))])
    return matrix_sum
