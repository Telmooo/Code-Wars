def matrix_mult(a, b):
    new_mx = []
    if len(a[0]) == len(b):
        for line in a:
            new_line = []
            for i in range(len(b[0])):
                new_line.append(sum(line[j]*b[j][i] for j in range(len(line))))
            new_mx.append(new_line)
    return new_mx
