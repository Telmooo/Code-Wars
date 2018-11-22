def lowest_product(x):
    if len(x) < 4: return "Number is too small"
    c = [x[i:i+4] for i in range(len(x)-3)]
    m = min(c, key= lambda x: int(x[0])*int(x[1])*int(x[2])*int(x[3]))
    return int(m[0])*int(m[1])*int(m[2])*int(m[3])
