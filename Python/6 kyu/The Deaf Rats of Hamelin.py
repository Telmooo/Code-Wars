def count_deaf_rats(town):
    p_loc = town.find("P")
    skip = False
    deaf_rats = 0
    for i, char in enumerate(town):
        if skip: skip = False; continue

        if char == "~":
            deaf_rats += 1 if i > p_loc else 0
            skip = True
            continue

        if char == "O":
            deaf_rats += 1 if i < p_loc else 0
            skip = True
            continue
    return deaf_rats
