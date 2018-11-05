def fake_bin(x):
    return "".join("1" if char >= "5" else "0" for char in x)
