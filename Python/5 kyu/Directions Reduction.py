def dirReduc(arr):
    ls = []
    last = ""
    changes = 0
    for i in arr:
        if i == "SOUTH" and last == "NORTH": ls.pop(); last = ""; changes += 1; continue
        if i == "NORTH" and last == "SOUTH": ls.pop(); last = ""; changes += 1; continue
        if i == "WEST" and last == "EAST": ls.pop(); last = ""; changes += 1; continue
        if i == "EAST" and last == "WEST": ls.pop(); last = ""; changes += 1; continue
        last = i; ls.append(i); continue 
    return dirReduc(ls) if changes else ls
