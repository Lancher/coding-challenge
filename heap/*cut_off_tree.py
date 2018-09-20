# LEETCODE@ 675. Cut Off Trees for Golf Event
#
# --END--


import heapq


def cutOffTree(self, forest):
    # validation
    if not forest or not forest[0]:
        return 0

    # init
    m, n = len(forest), len(forest[0])

    # heap to sort by heights
    h = []
    for i in range(m):
        for j in range(n):
            if forest[i][j] > 1:
                heapq.heappush(h, (forest[i][j], i, j))

    # current i, j
    cur = [0, 0]

    # total steps
    res = 0

    # get the lowest tree
    while h:
        height, ti, tj = heapq.heappop(h)

        # bfs
        step = 0
        q = [(cur[0], cur[1])]
        vst = set()
        can_reach = False

        # q contain valid node & not yet put into vst set.
        while q:
            next_q = []
            for i, j in q:
                if i == ti and j == tj:
                    res += step
                    can_reach = True
                    next_q = []
                    break
                else:
                    vst.add((i, j))
                    x, y = 0, 1
                    for _ in range(4):
                        x, y = y, -x
                        ni, nj = i + x, j + y
                        if 0 <= ni < m and 0 <= nj < n and forest[ni][nj] > 0 and (ni, nj) not in vst:
                            next_q.append((ni, nj))
            step += 1
            q = next_q

        # if we can reach next point return -1
        if can_reach:
            cur[0], cur[1] = ti, tj
        else:
            return -1

    return res
