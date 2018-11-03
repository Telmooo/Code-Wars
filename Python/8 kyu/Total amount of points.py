def points(games):
    return sum((x >= y) + 2 * (x > y) for x, y in (sets.split(":") for sets in games))
