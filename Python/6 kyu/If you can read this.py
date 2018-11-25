def to_nato(words):
    alphabet = {"a": "Alfa", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo", "f": "Foxtrot",
                   "g": "Golf", "h": "Hotel", "i": "India", "j": "Juliett", "k": "Kilo", "l": "Lima",
                   "m": "Mike", "n": "November", "o": "Oscar", "p": "Papa", "q": "Quebec", "r": "Romeo",
                   "s": "Sierra", "t": "Tango", "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "Xray",
                   "y": "Yankee", "z": "Zulu", ".": ".", "?": "?", "!": "!", ",": ","}
    return " ".join([alphabet.get(char.lower()) for char in words if char.lower() in alphabet])
