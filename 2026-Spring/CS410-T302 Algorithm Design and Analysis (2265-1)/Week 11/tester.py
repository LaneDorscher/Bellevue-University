from tests import generate_sudoku_tests
from sudoku_solver import solve_sudoku


def run_tests():
    sudoku_tests = generate_sudoku_tests()

    passed_tests = 0  # Counter for tests that pass

    for i, (input_board, expected_solution) in enumerate(sudoku_tests):
        print(f"Test {i + 1}/{len(sudoku_tests)}:")
        print("Input Sudoku Board:")
        print_board(input_board)

        solved_board = [row[:] for row in input_board]
        if solve_sudoku(solved_board):
            print("\nSolved Sudoku Board:")
            print_board(solved_board)

            # Check if the solved board matches the expected solution
            is_match = are_boards_equal(solved_board, expected_solution)

            if is_match:
                print("Test Result: Pass")
                passed_tests += 1  # Increment the counter if the test passed
            else:
                print("Test Result: Fail (Solved board does not match expected solution)")
        else:
            print("\nNo solution exists.")
            print("Test Result: Fail (No solution)")

        print("\n")

    # Print the summary at the end
    print(f"Total tests passed: {passed_tests}/{len(sudoku_tests)}")


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


def are_boards_equal(board1, board2):
    return all(row1 == row2 for row1, row2 in zip(board1, board2))


if __name__ == "__main__":
    run_tests()
