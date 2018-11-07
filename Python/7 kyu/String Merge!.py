def string_merge(string1, string2, letter):
    return "{0}{1}{2}".format(string1.split(letter, 1)[0], letter, string2.split(letter, 1)[1])
