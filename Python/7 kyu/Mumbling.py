def accum(s):
    code = ""
    i = 0
    for char in s:
        code += "{0}{1}-".format(char.upper(), char.lower()*i)
        i += 1
    return code[:-1]
