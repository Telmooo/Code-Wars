def play_pass(s, n):
    from string import ascii_letters as al
    shft_up = al[26:][n:] + al[26:][:n]
    shft_low = al[:26][n:] + al[:26][:n]

    code = str.maketrans(al, shft_low+shft_up)
    r = ""
    for i, char in enumerate(s):

        if ord(char) in code:
            c = chr(code[ord(char)])
            r += c.lower() if (i)%2 else c

        elif char.isdigit():
            r += f"{9-int(char)}"

        else: r += char

    return r[::-1]
