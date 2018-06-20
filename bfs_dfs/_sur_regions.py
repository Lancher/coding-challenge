# LEETCODE@ 130. Surrounded Regions
#
# 1) Run the bfs.
#
# --END--


def solve(self, board):
    if not board:
        return
    for i in range(len(board)):
        if board[i][0] == 'O':
            self.bfs(board, i, 0)
        if board[i][len(board[i]) - 1] == 'O':
            self.bfs(board, i, len(board[i]) - 1)
    for j in range(len(board[0])):
        if board[0][j] == 'O':
            self.bfs(board, 0, j)
        if board[len(board) - 1][j] == 'O':
            self.bfs(board, len(board) - 1, j)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == ' ':
                board[i][j] = 'O'


def bfs(self, board, i, j):
    q = []
    q.append((i, j))
    board[i][j] = ' '
    while q:
        p = q.pop()
        x, y = 0, 1
        for _ in range(4):
            x, y = y, -x
            if 0 <= p[0] + x < len(board) and 0 <= p[1] + y < len(board[0]):
                if board[p[0] + x][p[1] + y] == 'O':
                    q.append((p[0] + x, p[1] + y))
                    board[p[0] + x][p[1] + y] = ' '