# 787. Cheapest Flights Within K Stops
#
# 1. Use heap to simulate Dijkstras Algorithm
#
#               500
#     [0] -------------> [1]
#      \                  ^
#       \  100           / 100
#        \-----> [2] ---/
#
#
#   Push [500, 1] to heap doesn't matter, because it will stay on the bottom
#   of the heap.
#
#   Each element pop from is the nearest because Dijkstra Algorithm
#
#
# --END--
import heapq
import collections


def findCheapestPrice(self, n, flights, src, dst, K):
    # create map
    d = collections.defaultdict(dict)
    for f in flights:
        d[f[0]][f[1]] = f[2]

    # heap
    h = []
    heapq.heappush(h, [0, src, K + 1])

    # each element pop from is the nearest because Dijkstra Algorithm
    while h:
        w, i, k = heapq.heappop(h)
        if i == dst:
            return w
        if k > 0:
            for j in d[i]:
                heapq.heappush(h, [w + d[i][j], j, k - 1])

    return -1
