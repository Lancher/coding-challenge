# LEETCODE@ 794. Valid Tic-Tac-Toe State
#
# 1. Write all the rules.
#
# --END--


def validTicTacToe(self, board):
    n = 3
    x_cnt = 0
    o_cnt = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                x_cnt += 1
            if board[i][j] == 'O':
                o_cnt += 1
    if not 0 <= x_cnt - o_cnt <= 1:
        return False

    x_same = 0
    o_same = 0

    # h
    for i in range(n):
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            x_same += 1
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            o_same += 1
    # v
    for j in range(n):
        if board[0][j] == board[1][j] == board[2][j] == 'X':
            x_same += 1
        if board[0][j] == board[1][j] == board[2][j] == 'O':
            o_same += 1
    # dia
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        x_same += 1
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        o_same += 1
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        x_same += 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        o_same += 1

    if x_same and o_same:
        return False
    elif x_same and x_cnt - o_cnt != 1:
        return False
    elif o_same and x_cnt != o_cnt:
        return False
    else:
        return True
