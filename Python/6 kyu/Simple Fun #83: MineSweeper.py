def minesweeper(matrix):
    return list([count_mines(i, j, matrix) for j in range(len(matrix[i]))] for i in range(len(matrix)))
              

def count_mines(x, y, matrix):
    l, c = len(matrix), len(matrix[0])
    lines, cols = range(l), range(c)
    in_board = lambda x, y: x in lines and y in cols
    total = (matrix[(x-1)%l][(y-1)%c]*in_board(x-1, y-1) + matrix[x][(y-1)%c]*in_board(x, y-1) +
             matrix[(x+1)%l][(y-1)%c]*in_board(x+1, y-1) + matrix[(x-1)%l][y]*in_board(x-1, y) +
             matrix[(x+1)%l][y]*in_board(x+1, y) + matrix[(x-1)%l][(y+1)%c]*in_board(x-1, y+1) +
             matrix[x][(y+1)%c]*in_board(x, y+1) + matrix[(x+1)%l][(y+1)%c]*in_board(x+1, y+1))
    return total
