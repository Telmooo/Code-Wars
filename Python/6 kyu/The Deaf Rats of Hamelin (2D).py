def count_deaf_rats(town_square):
    from math import sqrt
    grid = [list(row) for row in town_square]

    x, y = 0, 0
    
    for i, line in enumerate(grid):
        for j, tile in enumerate(line):
            if tile == "P":
                x, y = (i, j)
                break
    
    deaf_rats = 0
    
    for i, line in enumerate(grid):
        for j, tile in enumerate(line):
            
            if tile == "↑":
                delta = sqrt((-x+i)**2 + (-y+j)**2) - sqrt((-x+i-1)**2 + (-y+j)**2)
                if delta < 0: deaf_rats += 1
            
            if tile == "↓":
                delta = sqrt((-x+i)**2 + (-y+j)**2) - sqrt((-x+i+1)**2 + (-y+j)**2)
                if delta < 0: deaf_rats += 1
                
            if tile == "←":
                delta = sqrt((-x+i)**2 + (-y+j)**2) - sqrt((-x+i)**2 + (-y+j-1)**2)
                if delta < 0: deaf_rats += 1
            
            if tile == "→":
                delta = sqrt((-x+i)**2 + (-y+j)**2) - sqrt((-x+i)**2 + (-y+j+1)**2)
                if delta < 0: deaf_rats += 1
            
            if tile == "↗":
                delta = sqrt((-x+i)**2 + (-y+j)**2) - sqrt((-x+i-1)**2 + (-y+j+1)**2)
                if delta < 0: deaf_rats += 1
            
            if tile == "↙":
                delta = sqrt((-x+i)**2 + (-y+j)**2) - sqrt((-x+i+1)**2 + (-y+j-1)**2)
                if delta < 0: deaf_rats += 1
            
            if tile == "↖":
                delta = sqrt((-x+i)**2 + (-y+j)**2) - sqrt((-x+i-1)**2 + (-y+j-1)**2)
                if delta < 0: deaf_rats += 1
            
            if tile == "↘":
                delta = sqrt((-x+i)**2 + (-y+j)**2) - sqrt((-x+i+1)**2 + (-y+j+1)**2)
                if delta < 0: deaf_rats += 1

    return deaf_rats
