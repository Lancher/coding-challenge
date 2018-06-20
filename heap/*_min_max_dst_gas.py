# LEETCODE@ 774. Minimize Max Distance to Gas Station
#
# 1. The idea is to use Greedy!!!
#
#   Put as much stations to the max distance in the heap!!!
#
# 2. It will happen Time Limit Exceeded, so we need some pre computation
#
# --END--


import heapq


def minmaxGasDist(self, stations, K):
    max_d = (stations[-1] - stations[0]) / K

    h = []
    for i in range(len(stations) - 1):
        # pre-computation to avoid timeout
        slots = max(1, int((stations[i + 1] - stations[i]) / max_d))
        K -= slots - 1
        heapq.heappush(h, [-(stations[i + 1] - stations[i]) / slots, i, i + 1, slots])

    for i in range(K):
        dst, i, j, slots = heapq.heappop(h)
        heapq.heappush(h, [-(stations[i + 1] - stations[i]) / (slots + 1), i, j, slots + 1])

    return -h[0][0]

