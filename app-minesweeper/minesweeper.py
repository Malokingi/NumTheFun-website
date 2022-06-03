import random
import re

class Board:
    def __init__(self, dim_width, dim_height, quant_mine):
        # store params
        self.dim_width = dim_width
        self.dim_height = dim_height
        self.quant_mine = quant_mine

        # make board
        self.board = self.make_new_board() # Makes board and adds mines
        self.assign_values_to_board() # Add numbers to all non-mine spaces

        # Track dug
        # Will contain coordinates of exposed spaces
        self.dug = set()

    def make_new_board(self):
        # Generate new Board
        board = [[None for _ in range(self.dim_width)] for _ in range(self.dim_height)]

        # Bury Mines
        mines_buried = 0
        while mines_buried < self.quant_mine:
            loc = random.randint(0, (self.dim_width * self.dim_height) - 1)
            #  |0|1|2|
            # 0|0|1|2|
            # 1|3|4|5|
            # 2|6|7|8|
            # 3|9|A|B|
            row = loc // self.dim_width # returns floor of loc / width, indicating the row e.g. loc = 7, w = 3, 7 / 3 = 2.33 => 2
            col = loc % self.dim_width # returns modulo of loc % width, indicating the col e.g. loc = 7, w = 3, 7 % 3 = 1

            if board[row][col] == '*':
                # There's already a mine there
                continue

            board[row][col] = '*' # put mine
            mines_buried += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_height):
            for c in range(self.dim_width):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_neighboring_mines_quant(r, c)
    
    def get_neighboring_mines_quant(self, row, col):
        quant = 0
        wraparound = False
        # Iterate thru up to 8 neighboring positions and count mines
        for r in range(max(0, row - 1), min(self.dim_height - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_width - 1, col + 1) + 1):
                if r == row and c == col:
                    # skip
                    continue
                if self.board[r][c] == '*':
                    quant += 1

        return quant

    def dig(self, row, col):
        # return false if it's a mine, true otherwise
        self.dug.add((row, col)) # flag this space as dug

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        # The remaining possibility, self.board[row][col] == 0 is covered below since we've already returned out of this function otherwise
        for r in range(max(0, row - 1), min(self.dim_height - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_width - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue # This space is already uncovered
                self.dig(r, c)
        
        return True # If all the spaces near mines are marked correctly, we should never encounter a mine in this recursive loop

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_width)] for _ in range(self.dim_height)]
        for row in range(self.dim_height):
            for col in range(self.dim_width):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        string_rep = ''
        widths = []
        for idx in range(self.dim_width):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        
        indicies = [i for i in range(self.dim_width)]
        indicies_row = '   '
        cells = []
        for idx, col in enumerate(indicies):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indicies_row += '  '.join(cells)
        indicies_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += '  '.join(cells)
            string_rep += '  \n'
        
        str_len = int(len(string_rep) / self.dim_width)
        string_rep = indicies_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep

# play the game
def play(dim_width=5, dim_height=9, quant_mine=6):
    # Step 1: Make Board and place mines
    board = Board(dim_width, dim_height, quant_mine)

    # Step 2: Display board and ask user where to dig
    # Step 3a: If location is a mine, show game over message
    # Step 3b: If location is next to a mine, display Number
    # Step 3c: If location is not near a mine, Recursivly dig until each exposed space is next to a mine
    # Step 4: Repeat Steps 2 and 3 until all non-mine spaces are found
    safe = True
    while len(board.dug) < ((dim_width * dim_height) - quant_mine):
        print(board)
        user_input = re.split('', input("Pick a space in the format [row],[col]: "))
        print(user_input)
        row, col = int(user_input[1]), int(user_input[-2])
        if row < 0 or col < 0 or row >= board.dim_height or col >= board.dim_width:
            print("Invalid Location. Pick a row and col within range.")
            continue

        safe = board.dig(row, col) # True is there's no mine here
        if not safe:
            break

    if safe:
        print("You made it! Congratulations")
    else:
        print("Game Over. You died.")

    board.dug = [(r, c) for r in range(board.dim_height) for c in range(board.dim_width)]
    print(board)

if __name__ == '__main__':
    play()