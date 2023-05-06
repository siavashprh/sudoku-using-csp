class SudokuSolver:
    def __init__(self, board):
        self.board = board
    
    def solve(self):
        if self.is_complete():
            return self.board

        row, col = self.select_unassigned_variable()

        for value in self.get_ordered_domain_values(row, col):
            if self.is_consistent(row, col, value):
                self.board[row][col] = value

                if self.solve():
                    return self.board

                self.board[row][col] = 0

        return False

    def is_complete(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        return True

    def select_unassigned_variable(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None

    def get_ordered_domain_values(self, row, col):
        domain = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        row_values = set(self.board[row])
        col_values = set([self.board[i][col] for i in range(9)])
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        box_values = set([
            self.board[i][j]
            for i in range(box_row, box_row + 3)
            for j in range(box_col, box_col + 3)
        ])
        return list(domain - row_values - col_values - box_values)

    def is_consistent(self, row, col, value):
        row_values = set(self.board[row])
        if value in row_values:
            return False

        col_values = set([self.board[i][col] for i in range(9)])
        if value in col_values:
            return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        box_values = set([
            self.board[i][j]
            for i in range(box_row, box_row + 3)
            for j in range(box_col, box_col + 3)
        ])
        if value in box_values:
            return False

        return True


def solve_sudoku(board):
    solver = SudokuSolver(board)
    return solver.solve()

# Example usage:
# board = [
#     [5, 3, 4, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9],
# ]

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
c = int(input())
for _ in range(c):
    i, j, value = map(int, input().split())
    i -= 1
    j -= 1
    board[i][j] = value

solver = SudokuSolver(board)
solution = solver.solve()

if solution:
    print("Solved board:")
    for row in solution:
        print(row)
else:
    print("No solution found")

