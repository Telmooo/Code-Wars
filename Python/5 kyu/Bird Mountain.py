def peak_height(mountain):
    
    def in_bounds(matrix, i, j):
        return 0<=i<len(matrix) and 0<=j<len(matrix[i])
    
    height = 0
    changes = False
    while True:
        for i, row in enumerate(mountain):
            mountain[i] = list(row)
            for j, char in enumerate(row):
                if char == "^":
                    for k in range(-1, 2, 2):
                        if not (in_bounds(mountain, i, j+k) and in_bounds(mountain, i+k, j)):
                            mountain[i][j] = 1
                            changes = True
                            break
                        
                        if mountain[i][j+k] == " " or mountain[i][j+k] == 0:
                            mountain[i][j] = 1
                            changes = True
                            break
                        
                        if mountain[i+k][j] == " " or mountain[i][j+k] == 0:
                            mountain[i][j] = 1
                            changes = True
                            break
                        
                        if mountain[i][j+k] == height:
                            mountain[i][j] = height + 1
                            changes = True
                            break
                        
                        if mountain[i+k][j] == height:
                            mountain[i][j] = height + 1
                            changes = True
                            break
 
                elif char == " ":
                    mountain[i][j] = 0
                
                else:
                    continue
        
        if not changes:
            break
        height += 1
        changes = False

    return height
