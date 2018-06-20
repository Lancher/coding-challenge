# LEETCODE@ 79. Word Search
#
# 1. Just the simple backtracing.
#
# --END


def exist(self, board, word):
    res = [False]
    for i in range(len(board)):
        for j in range(len(board[i])):
            self.backtracing(board, i, j, word, 0, res)
    return res[0]


def backtracing(self, board, i, j, word, k, res):
    if res[0]:
        return
    if k == len(word):
        res[0] = True
    else:
        if 0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] == word[k]:
            ch = board[i][j]
            board[i][j] = ' '
            self.backtracing(board, i + 1, j, word, k + 1, res)
            self.backtracing(board, i - 1, j, word, k + 1, res)
            self.backtracing(board, i, j + 1, word, k + 1, res)
            self.backtracing(board, i, j - 1, word, k + 1, res)
            board[i][j] = ch


# LEETCODE@ 212. Word Search II
#
# --END--


def findWords(self, board, words):
    # 1. when facing dictionaries, you have to build trie to redcue search time
    root = {}
    for w in words:
        node = root
        for c in w:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['END'] = {}

    l, res = [], []
    for i in range(len(board)):
        for j in range(len(board[i])):
            self.backtracing(board, i, j, root, l, res)

    # [["a","a"]]
    # ["a"]
    return list(set(res))


def backtracing(self, board, i, j, node, l, res):
    # 2. deal the i, j first to find the matching string
    if board[i][j] not in node:
        return

    # 3. push the character
    ch = board[i][j]
    board[i][j] = ' '
    l.append(ch)

    if 'END' in node[ch]:
        res.append(''.join(l))

    # 4. add 4 points
    x, y = 0, 1
    for _ in range(4):
        x, y = y, -x
        if 0 <= i + x < len(board) and 0 <= j + y < len(board[i]) and board[i + x][j + y] != ' ':
            self.backtracing(board, i + x, j + y, node[ch], l, res)

    # 5. pop the character
    board[i][j] = ch
    l.pop()
