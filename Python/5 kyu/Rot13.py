import string
from codecs import encode as _dont_use_this_

def rot13(message):
    alph_lower = string.ascii_lowercase
    alph_upper = string.ascii_uppercase
    code = ""
    for char in message:
         if char.isupper():
             code += alph_upper[(alph_upper.index(char)+13)%26]
         elif char.islower():
             code += alph_lower[(alph_lower.index(char)+13)%26]
         else: code += char
    return code
