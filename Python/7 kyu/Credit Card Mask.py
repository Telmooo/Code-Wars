# return masked string
def maskify(cc):
    code = cc
    if len(cc) > 4:
        char = list(cc)
        for i in range(len(char)-4):
            char[i] = "#"
        code = "".join(char)
    return code
