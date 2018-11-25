def decode(string):
    morse = {".-": "a", "....": "h", "---": "o", "..-": "u", ".----": "1", "-....": "6",
             "-...": "b", "..": "i", ".--.": "p", "...-": "v", "..---": "2", "--...": "7",
             "-.-.": "c", ".---": "j", "--.-": "q", ".--": "w", "...--": "3", "---..": "8",
             "-..": "d", "-.-": "k", ".-.": "r", "-..-": "x", "....-": "4", "----.": "9",
             ".": "e", ".-..": "l", "...": "s", "-.--": "y", ".....": "5", "-----": "0",
             "..-.": "f", "--": "m","-": "t", "--..": "z",
             "--.": "g", "-.": "n" 
            }
    if not string: return ""
    phrase = string.split("  ")
    r = ()
    for word in phrase:
        r += ("".join(morse[c] for c in word.split(" ")),)
    return " ".join(r)