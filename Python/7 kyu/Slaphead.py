def bald(s):
    shave = "-"*len(s)
    hairs = s.count("/")
    if hairs == 0: return [shave, "Clean!"]
    if hairs == 1: return [shave, "Unicorn!"]
    if hairs == 2: return [shave, "Homer!"]
    if 3 <= hairs <= 5: return [shave, "Careless!"]
    if hairs > 5: return [shave, "Hobo!"]
