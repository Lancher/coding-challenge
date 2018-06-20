# Single source shortest path: shortest path from S to all other points.
#
# 1. No negative weight allowed!!!
#
# 2. http://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/
#
# 3. https://www.youtube.com/watch?v=oJ9iR9QRsl0
#
# --END--

import heapq


def dijkstra(g):
    n = len(g)

    dst = [-1] * n

    h = []
    heapq.heappush(h, [0, 0])

    while h:
        # each pop element is the shortest element
        w, i = heapq.heappop(h)
        if dst[i] == -1:
            dst[i] = w

            # each node will be set only one time
            n -= 1
            if n == 0:
                break

        # put adjacent nodes into heap
        for j in g[i]:
            heapq.heappush(h, [w + g[i][j], j])

    return dst


g = {
    0: {1: 5.0, 4: 9.0, 7: 8.0},
    1: {2: 12.0, 3: 15.0, 7: 4.0},
    2: {3: 3.0, 6: 11.0},
    3: {6: 9.0},
    4: {5: 4.0, 6: 20.0, 7: 5.0},
    5: {2: 1.0, 6: 13.0},
    6: {},
    7: {2: 7.0, 5: 6.0},
}
print(dijkstra(g))
