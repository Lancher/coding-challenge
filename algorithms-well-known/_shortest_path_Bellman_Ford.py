# Bellman Ford algorithm
#
# 1. Idea:
#
#   Go through all vertices and relax the edges N times
#
# 2. Video:
#
#   https://www.youtube.com/watch?v=HoGSiB7tSeI&list=PLxc4gS-_A5VDvP_9W8JJ04zk6m1qTolzG&index=23
#
# --END


def bellman_ford(g):
    n = len(g)

    # distance
    dst = [float('inf')] * len(g)
    dst[0] = 0

    # iterate n times
    for _ in range(n):

        # iterate each edges
        for i in range(n):
            for j in g[i]:
                if dst[i] + g[i][j] < dst[j]:
                    dst[j] = dst[i] + g[i][j]

    # do one more time to detect negative weight
    for i in range(n):
        for j in g[i]:
            if dst[i] + g[i][j] < dst[j]:
                print("negative weight happen")

    # return dst
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
print(bellman_ford(g))
