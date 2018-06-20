# LEETCODE@ 218. The Skyline Problem
#
# 1) https://www.youtube.com/watch?v=GSBLe8cKu0s
#
# Python does not have heap.remove() function
#
# --END--


from heapq import *


def getSkyline(self, LRH):
    skyline = []
    i, n = 0, len(LRH)
    liveHR = []
    while i < n or liveHR:
        if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
            x = LRH[i][0]
            while i < n and LRH[i][0] == x:
                heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                i += 1
        else:
            x = -liveHR[0][1]
            while liveHR and -liveHR[0][1] <= x:
                heappop(liveHR)
        height = len(liveHR) and -liveHR[0][0]
        if not skyline or height != skyline[-1][1]:
            skyline += [x, height],
    return skyline
