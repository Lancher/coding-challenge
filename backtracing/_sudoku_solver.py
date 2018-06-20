# LEETCODE@ 37. Sudoku Solver
#
# In backtracing, if we want to return original matrix, make sure we dont not set the the value
# back when we reach one solution.
#
# --END--


def solveSudoku(self, board):
    n = len(board)
    row = [[0] * 9 for _ in range(9)]
    col = [[0] * 9 for _ in range(9)]
    box = [[0] * 9 for _ in range(9)]

    # prefix counting
    for i in range(n):
        for j in range(n):
            if board[i][j] != '.':
                v = int(board[i][j]) - 1
                row[i][v] = col[j][v] = box[int(i / 3) * 3 + int(j / 3)][v] = 1

    res = [0]
    self.backtracing(board, n, 0, row, col, box, res)


def backtracing(self, board, n, k, row, col, box, res):
    if k == n * n:
        res[0] = 1
    else:
        # find the '.'
        while k < n * n and board[int(k / n)][int(k % n)] != '.':
            k += 1
        # reach the end
        if k == n * n:
            res[0] = 1
            return

        i, j = int(k / n), int(k % n)
        for v in range(1, 10):
            if not row[i][v - 1] and not col[j][v - 1] and not box[int(i / 3) * 3 + int(j / 3)][v - 1]:
                row[i][v - 1] = col[j][v - 1] = box[int(i / 3) * 3 + int(j / 3)][v - 1] = 1
                board[i][j] = str(v)
                self.backtracing(board, n, k + 1, row, col, box, res)
                if not res[0]:
                    row[i][v - 1] = col[j][v - 1] = box[int(i / 3) * 3 + int(j / 3)][v - 1] = 0
                    board[i][j] = '.'
