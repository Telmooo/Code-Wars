def replace_exclamation(s):
    return "".join("!" if x.lower() in "aeiou" else x for x in s)
