
# 773. Sliding Puzzle
#
# 1. Sometimes, you have to start from END [[1, 2, 3], [5, 6, 0]] to reach the answer
#
# 2. Use `bfs` to walk the every possibilities and
#
# --END--
import copy


def slidingPuzzle(self, board):
    init_b = [[1, 2, 3], [4, 5, 0], [1, 2]]
    res = 0
    s = set()
    q = [init_b]

    while q:
        next_q = []
        for b in q:
            if [b[0], b[1]] == board:
                return res
            else:
                key = str(b[0][0]) + str(b[0][1]) + str(b[0][2]) + str(b[1][0]) + str(b[1][1]) + str(b[1][2])
                if key in s:
                    continue
                else:
                    s.add(key)
                i, j = b[-1][0], b[-1][1]
                if i == 0:
                    cp_b = copy.deepcopy(b)
                    cp_b[i][j], cp_b[i + 1][j] = cp_b[i + 1][j], cp_b[i][j]
                    cp_b[-1][0] = cp_b[-1][0] + 1
                    next_q.append(cp_b)
                if i == 1:
                    cp_b = copy.deepcopy(b)
                    cp_b[i][j], cp_b[i - 1][j] = cp_b[i - 1][j], cp_b[i][j]
                    cp_b[-1][0] = cp_b[-1][0] - 1
                    next_q.append(cp_b)
                if j > 0:
                    cp_b = copy.deepcopy(b)
                    cp_b[i][j], cp_b[i][j - 1] = cp_b[i][j - 1], cp_b[i][j]
                    cp_b[-1][1] = cp_b[-1][1] - 1
                    next_q.append(cp_b)
                if j < 2:
                    cp_b = copy.deepcopy(b)
                    cp_b[i][j], cp_b[i][j + 1] = cp_b[i][j + 1], cp_b[i][j]
                    cp_b[-1][1] = cp_b[-1][1] + 1
                    next_q.append(cp_b)
        res += 1
        q = next_q
    return -1
