from collections import Set

board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]
place = []
pos = 0
rows = []
columns = []
squares = []
step = 0
# curr = []
previously_placed = 0
s = Set()
x = 0
y = 0


def square_number(r, c):
    actualRow = r / 3
    actualCol = c / 3
    return (actualRow * 3) + actualCol


def add_row_to_set(j):
    s = Set()
    for i in range(9):
        if board[i][j] != '.':
            s.add(board[i][j])


def add_column_to_set(i):
    s = Set()
    for j in range(9):
        if board[i][j] != '.':
            s.add(board[i][j])


def add_square_to_set(i, j):
    s = Set()
    for i in range(0, 8, 3):
        for j in range(0, 8, 3):
            if board[i][j] != '.':
                s.add(board[i][j])


for i in range(9):
    for j in range(9):
        if board[i][j] == '.':
            place.append([i][j])

for i in range(9):
    rows.append(add_row_to_set(i))

for i in range(9):
    columns.append(add_column_to_set(i))

for i in range(9):
    squares.append(add_square_to_set(i))

def solve_board(board, place, pos, forward, rows, columns, squares):
    if step < 50:
        if pos == len(place):
            print("done")
        else:
            curr = place.get(pos)
            if forward:

                x = curr[0]
                y = curr[1]
                for i in range(1, 9):
                    if i not in rows.get(x) and i not in columns.get(y) and i not in squares.get(
                            square_number(x, y)):
                        board[x][y] = '' + i + ''
                        rows.get(x).add('' + i + '')
                        columns.get(y).add('' + i + '')
                        squares.get(square_number(x, y))
                        solve_board(pos + 1, True)
                solve_board(pos - 1, False)
            else:
                previously_placed = board[curr[0]][curr[1]])