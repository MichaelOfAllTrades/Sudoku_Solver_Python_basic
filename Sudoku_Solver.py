class Sudoku_Solver:

    def __init__(self, board):
        self.board = board
        self.place = []
        self.sub_place = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    self.sub_place = [i, j]
                    self.place.append(self.sub_place)
        print("place:")
        print(self.place)
        self.pos = 0
        self.curr = []
        self.x = 0
        self.y = 0

        self.rows = []
        for i in range(9):
            self.rows.append(self.add_row_to_set(i))
        print(self.rows)

        self.columns = []
        for i in range(9):
            self.columns.append(self.add_column_to_set(i))
        print(self.columns)

        self.squares = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                self.squares.append(self.add_square_to_set(i, j))
        print(self.squares)

        self.step = 0
        self.forward = True
        self.prev_placed = 0

        self.solve_board_while()

    def add_row_to_set(self, i):
        return {self.board[i][j] for j in range(9) if self.board[i][j] != '.'}

    def add_column_to_set(self, j):
        return {self.board[i][j] for i in range(9) if self.board[i][j] != '.'}

    def add_square_to_set(self, i, j):
        return {self.board[l][r] for l in range(i, i+3) for r in range(j, j+3) if self.board[l][r] != '.'}

    def square_number(self, r, c):
        # actual_row = r / 3
        # actual_col = c / 3
        # return int((actual_row * 3) + actual_col) - 1
        if r == 0 or r == 1 or r == 2:
            if c == 0 or c == 1 or c == 2:
                return 0
            if c == 3 or c == 4 or c == 5:
                return 1
            if c == 6 or c == 7 or c == 8:
                return 2
        if r == 3 or r == 4 or r == 5:
            if c == 0 or c == 1 or c == 2:
                return 3
            if c == 3 or c == 4 or c == 5:
                return 4
            if c == 6 or c == 7 or c == 8:
                return 5
        if r == 6 or r == 7 or r == 8:
            if c == 0 or c == 1 or c == 2:
                return 6
            if c == 3 or c == 4 or c == 5:
                return 7
            if c == 6 or c == 7 or c == 8:
                return 8

    def solve_board_while(self):
        self.curr = self.place[len(self.place)-1]
        self.x = self.curr[0]
        self.y = self.curr[1]
        while self.board[self.place[len(self.place)-1][0]][self.place[len(self.place)-1][1]] == '.':
            self.print_everything()
            self.step += 1
            self.curr = self.place[self.pos]
            self.x = self.curr[0]
            self.y = self.curr[1]
            if self.forward:
                progress = False
                for i in range(1, 10):
                    print(str(i) + " in row? " + str(chr(i+48) in self.rows[self.x]))
                    print(str(i) + " in column? " + str(chr(i+48) in self.columns[self.y]))
                    print(str(i) + " in square " + str(self.square_number(self.x, self.y)) + "? " + str(chr(i+48) in self.squares[self.square_number(self.x, self.y)]))
                    if chr(i+48) not in self.rows[self.x] and chr(i+48) not in self.columns[self.y] and chr(i+48) not in self.squares[self.square_number(self.x, self.y)]:
                        self.board[self.x][self.y] = chr(i+48)
                        self.rows[self.x].add(chr(i+48))
                        self.columns[self.y].add(chr(i+48))
                        self.squares[self.square_number(self.x, self.y)].add(chr(i+48))
                        self.pos += 1
                        self.forward = True
                        progress = True
                        print("placed a " + str(i) + " at " + str(self.x) + "," + str(self.y))
                        break
                if not progress:
                    self.pos -= 1
                    self.forward = False
            else:
                self.prev_placed = self.board[self.x][self.y]
                # print("prev placed = " + self.prev_placed)
                # print("rows length b4 remove = " + str(len(self.rows[self.x])))
                self.rows[self.x].remove(self.prev_placed)
                # print("rows length after remove = " + str(len(self.rows[self.x])))
                self.columns[self.y].remove(self.prev_placed)
                self.squares[self.square_number(self.x, self.y)].remove(self.prev_placed)

                progress = False;

                for i in range(int(self.prev_placed)+1, 10):
                    # print(chr(i+48))
                    if chr(i+48) not in self.rows[self.x] and chr(i+48) not in self.columns[self.y] and chr(i+48) not in self.squares[self.square_number(self.x, self.y)]:
                        self.board[self.x][self.y] = chr(i+48)
                        self.rows[self.x].add(chr(i+48))
                        self.columns[self.y].add(chr(i+48))
                        self.squares[self.square_number(self.x, self.y)].add(chr(i+48))
                        self.pos += 1
                        self.forward = True
                        progress = True
                        break
                if not progress:
                    self.board[self.x][self.y] = '.'
                    self.pos -= 1
                    self.forward = False
            print("\n")

    def solve_board(self):
        # self.print_everything()
        if self.step < 1500:
            self.step += 1
            if self.step % 5 == 0:
                print("step: " + str(self.step) + " pos: " + str(self.pos))
            if self.pos < len(self.place):
                self.curr = self.place[self.pos]
                self.x = self.curr[0]
                self.y = self.curr[1]

                # print("7 in current list?")
                # print(chr(7 + 48) not in self.rows[self.x] and chr(7 + 48) not in self.columns[self.y] and chr(
                #     7 + 48) not in self.squares[self.square_number(self.x, self.y)])

                if self.forward:
                    for i in range(1, 10):
                        # print(str(i) + " in row? " + str(chr(i+48) in self.rows[self.x]))
                        # print(str(i) + " in column? " + str(chr(i+48) in self.columns[self.y]))
                        # print(str(i) + " in square " + str(self.square_number(self.x, self.y)) + "? " + str(chr(i+48) in self.squares[self.square_number(self.x, self.y)]))
                        if chr(i+48) not in self.rows[self.x] and chr(i+48) not in self.columns[self.y] and chr(i+48) not in self.squares[self.square_number(self.x, self.y)]:
                            self.board[self.x][self.y] = chr(i+48)
                            self.rows[self.x].add(chr(i+48))
                            self.columns[self.y].add(chr(i+48))
                            self.squares[self.square_number(self.x, self.y)].add(chr(i+48))
                            self.pos += 1
                            self.forward = True
                            # print(str(i) + " added at " + str(self.x) + ","+ str(self.y))
                            # print("\n")
                            self.solve_board()
                    self.pos -= 1
                    self.forward = False
                    # print("\n")
                    self.solve_board()
                else:
                    self.prev_placed = self.board[self.x][self.y]
                    # print("prev placed = " + self.prev_placed)
                    # print("rows length b4 remove = " + str(len(self.rows[self.x])))
                    self.rows[self.x].remove(self.prev_placed)
                    # print("rows length after remove = " + str(len(self.rows[self.x])))
                    self.columns[self.y].remove(self.prev_placed)
                    self.squares[self.square_number(self.x, self.y)].remove(self.prev_placed)

                    for i in range(int(self.prev_placed)+1, 10):
                        # print(chr(i+48))
                        if chr(i+48) not in self.rows[self.x] and chr(i+48) not in self.columns[self.y] and chr(i+48) not in self.squares[self.square_number(self.x, self.y)]:
                            self.board[self.x][self.y] = chr(i+48)
                            self.rows[self.x].add(chr(i+48))
                            self.columns[self.y].add(chr(i+48))
                            self.squares[self.square_number(self.x, self.y)].add(chr(i+48))
                            self.pos += 1
                            self.forward = True
                            # print("\n")
                            self.solve_board()
                    self.board[self.x][self.y] = '.'
                    self.pos -= 1
                    self.forward = False
                    # print("\n")
                    self.solve_board()

    def print_everything(self):
        print("step: " + str(self.step))
        for arr in self.board:
            print(arr)
        print(self.pos)
        print(self.place[self.pos])
        print(self.rows)
        print(self.columns)
        print(self.squares)

    # https://pysnakeblog.blogspot.com/2019/09/python-underline-string-python.html
    # def print_board_with_underlines(self):
    #     for i in range(0, 8):
    #         for j in range(0, 8):
    #             if ()