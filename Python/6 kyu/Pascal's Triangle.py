def pascals_triangle(n):
    if n == 1: return [1]
    pascal = [[1]]
    r = [1]
    for i in range(1, n):
        line = []
        for j in range(i+1):
            if j == 0 or j==i: line.append(1)
            else: line.append(pascal[i-1][j-1]+pascal[i-1][j])
        pascal.append(line)
        r += line
    return r
