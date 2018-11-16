def score(dice):
    occurence = {x: dice.count(x) for x in dice}
    return sum([600 * (occurence.get(6, 0) // 3), 400 * (occurence.get(4, 0) // 3),
                300 * (occurence.get(3, 0) // 3), 200 * (occurence.get(2, 0) // 3),
                1000 * (occurence.get(1, 0) // 3), 500 * (occurence.get(5, 0) // 3),
                100 * (occurence.get(1, 0)%3), 50 * (occurence.get(5, 0)%3)])
