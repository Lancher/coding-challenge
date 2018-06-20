# LEETCODE@ 286. Walls and Gates
#
# 1) Put all the gates into queue, and run the dfs on each level.
#
# --END--


def wallsAndGates(self, rooms):
    if not rooms or not rooms[0]:
        return
    m, n = len(rooms), len(rooms[0])
    q = []
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            if rooms[i][j] == 0:
                q.append([i, j])

    dst = 0
    while q:
        next_q = []
        dst += 1
        for i, j in q:
            x, y = 1, 0
            for _ in range(4):
                x, y = y, -x
                ii, jj = i + x, j + y
                if 0 <= ii < m and 0 <= jj < n:
                    if dst < rooms[ii][jj]:
                        rooms[ii][jj] = dst
                        next_q.append([ii, jj])
        q = next_q
