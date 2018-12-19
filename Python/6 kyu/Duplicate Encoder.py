def duplicate_encode(word):
    occurences = {}
    code = ""
    for char in word.lower():
        if char not in occurences: occurences[char] = word.lower().count(char)
        if char in occurences:
            code += "(" if occurences[char]==1 else ")"
    return code
