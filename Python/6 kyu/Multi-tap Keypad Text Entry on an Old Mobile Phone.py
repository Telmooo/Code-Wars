def presses(phrase):
    presses = ["", "ADGJMPTW*#1 ", "BEHKNQUX0", "CFILORVY", "SZ234568", "79"]
    return sum(presses.index(key) for char in phrase for key in presses if char.upper() in key)
