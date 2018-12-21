def how_many_bees(hive):
    if hive is None: return 0
    bees = 0
    for i, comb in enumerate(hive):
        for j, cell in enumerate(comb):
            if cell == "b":
                if i > 1:
                    if (hive[i-1][j] == "e" and hive[i-2][j] == "e"): bees += 1
                if i < len(hive)-2:
                    if (hive[i+1][j] == "e" and hive[i+2][j] == "e"): bees += 1
                if j > 1:
                    if (hive[i][j-1] == "e" and hive[i][j-2] == "e"): bees += 1
                if j < len(hive[0])-2:
                    if (hive[i][j+1] == "e" and hive[i][j+2] == "e"): bees += 1
    return bees
