def board(inp):
    game = list(l[1:-1] for l in inp[1:-1])
    sol = [inp[0]]
    for i in range(len(game)):
        line = ""
        for j in range(len(game[0])):
            if game[i][j] == "*": line += "*"
            else:
                m = count_mines(i, j, game)
                line += str(m) if m else " "
        sol.append(f"|{line}|")
    sol.append(inp[-1])
    return sol
def count_mines(x, y, matrix):
    l, c = len(matrix), len(matrix[0])
    lines, cols = range(l), range(c)
    in_board = lambda x, y: x in lines and y in cols
    total = ((matrix[(x-1)%l][(y-1)%c]=="*")*in_board(x-1, y-1) + (matrix[x][(y-1)%c]=="*")*in_board(x, y-1) +
             (matrix[(x+1)%l][(y-1)%c]=="*")*in_board(x+1, y-1) + (matrix[(x-1)%l][y]=="*")*in_board(x-1, y) +
             (matrix[(x+1)%l][y]=="*")*in_board(x+1, y) + (matrix[(x-1)%l][(y+1)%c]=="*")*in_board(x-1, y+1) +
             (matrix[x][(y+1)%c]=="*")*in_board(x, y+1) + (matrix[(x+1)%l][(y+1)%c]=="*")*in_board(x+1, y+1))
    return total
