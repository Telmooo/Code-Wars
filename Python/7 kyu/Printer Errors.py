def printer_error(s):
    return "{0}/{1}".format(sum(letter > "m" for letter in s), len(s))
