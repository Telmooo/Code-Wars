def getMatrixProduct(M, N):
    new_mx = []
    if len(M[0]) == len(N):
        for line in M:
            new_line = []
            for i in range(len(N[0])):
                new_line.append(sum(line[j]*N[j][i] for j in range(len(line))))
            new_mx.append(new_line)
    return new_mx if new_mx else -1
