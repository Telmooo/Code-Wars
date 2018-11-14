def max_match(sentence):
    ls = []
    astr = sentence
    while len(astr):
        for  i in range(len(astr), 0, -1):
            substr = astr[:i]
            if substr in VALID_WORDS:
                break
        ls.append(substr)
        astr = astr[i:]
    return ls
