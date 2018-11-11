def loose_change(cents):
    change_dict = {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}
    if cents > 0:
        for coin, value in zip(("Quarters", "Dimes", "Nickels", "Pennies"), (25, 10, 5, 1)):
            change_dict[coin] = cents // value
            cents -= value*change_dict[coin]
    return change_dict
