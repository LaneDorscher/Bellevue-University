def is_valid(board, row, col, num):
    """
    Determine if it's valid to place 'num' at position (row, col) on the Sudoku board.
    Implement the necessary checks.
    """

    for x in range(9):
        # check target row
        if (board[row][x] == num): return False
        # check target column
        if (board[x][col] == num): return False
    
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col+3):
            if (board[r][c] == num): return False

    return True


def solve_sudoku(board):
    """
    Solve the provided Sudoku board using backtracking.
    Fill in the solution directly into the board.
    Return True if a solution exists, otherwise return False.
    """
    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range (1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    
    return True          



if __name__ == "__main__":
    import sys

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py <input_file>")
        sys.exit(1)

    # Read Sudoku board from the input file
    input_file = sys.argv[1]
    with open(input_file, "r") as file:
        sudoku_board = [[int(num) for num in line.split()] for line in file.readlines()]

    print("Input Sudoku Board:")
    for row in sudoku_board:
        print(" ".join(map(str, row)))

    # Solve the Sudoku board
    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        for row in sudoku_board:
            print(" ".join(map(str, row)))
    else:
        print("\nNo solution exists.")
