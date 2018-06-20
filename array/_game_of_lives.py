# LEETCODE@ 289. Game of Life
#
# 1. Use bits to represent:
#
#   00 -> 10   0 -> 2
#   01 -> 11   1 -> 3
#
# --END--


def gameOfLife(self, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            lives = self.numberOfLives(board, i, j)
            # current alive
            if board[i][j]:
                if lives == 2 or lives == 3:
                    board[i][j] = 3
            # current dead
            else:
                if lives == 3:
                    board[i][j] = 2

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = board[i][j] >> 1


def numberOfLives(board, i, j):
    lives = 0
    for x in range(max(0, i - 1), min(i + 2, len(board))):
        for y in range(max(0, j - 1), min(j + 2, len(board[i]))):
            lives += board[x][y] & 1

    lives -= board[i][j] & 1
    return lives
