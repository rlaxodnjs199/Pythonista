# Sudoku Background
# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)

# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
import itertools

def check_sub_grid(sub_grid):
    return len(sub_grid) == 9 and sum(set(sub_grid)) == 45

def valid_solution(board):
    for row in board:
        if not check_sub_grid(row):
            return False
    for col in list(map(list, zip(*board))):
        if not check_sub_grid(col):
            return False
    for sub_grid_row in range(0, len(board), 3):
        for sub_grid_col in range(0, len(board[0]), 3):
            sub_grid = [row[sub_grid_row:sub_grid_row+3] for row in board[sub_grid_col:sub_grid_col+3]]
            sub_grid_flattened = list(itertools.chain(*sub_grid))
            if not check_sub_grid(sub_grid_flattened):
                return False
    return True


if __name__ == '__main__':
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    print(valid_solution(board))