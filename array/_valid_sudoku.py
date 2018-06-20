# LEETCODE@ 36. Valid Sudoku
#
# 1. Box is [0, 1, 2]
#           [3, 4, 5]
#           [6, 7, 8]
#
# --END--


def isValidSudoku(board):
    row = [[0] * 9 for _ in range(9)]
    col = [[0] * 9 for _ in range(9)]
    box = [[0] * 9 for _ in range(9)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                continue
            val = int(board[i][j]) - 1
            if row[i][val] or col[j][val] or box[int(i / 3) * 3 + int(j / 3)][val]:
                return False
            row[i][val] = col[j][val] = box[int(i / 3) * 3 + int(j / 3)][val] = 1
    return True
