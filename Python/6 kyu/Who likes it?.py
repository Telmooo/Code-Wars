def likes(names):
    l = len(names)
    if l == 0: return "no one likes this"
    elif l == 1: return "{} likes this".format(names[0])
    elif l == 2: return "{} like this".format(" and ".join(names))
    elif l == 3: return "{} and {} like this".format(", ".join(names[:2]), names[2])
    else: return "{} and {} others like this".format(", ".join(names[:2]), l-2)
