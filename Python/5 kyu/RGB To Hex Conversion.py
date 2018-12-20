rgb = lambda r, g, b: "".join(hex(x)[2:].upper().zfill(2) if 0<=x<=255 else "00" if x<0 else "FF" for x in [r, g, b])
