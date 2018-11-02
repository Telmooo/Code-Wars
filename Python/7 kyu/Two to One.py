def longest(s1, s2):
    chars = []
    for char in s1:
        if char not in chars:
            chars.append(char)
    for char in s2:
        if char not in chars:
            chars.append(char)
    chars.sort()
    return "".join(chars)
