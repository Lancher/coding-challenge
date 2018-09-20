# LEETCODE@ 630 Course Schedule III
#
# 1. A rigorous proof of optimality for this greedy algorithm.
#
#   https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
#
# --END--


import heapq


def scheduleCourse(self, courses):
    pq = []
    start = 0
    courses.sort(key=lambda k: k[1])
    for t, end in courses:
        start += t
        heapq.heappush(pq, -t)
        while start > end:
            start += heapq.heappop(pq)
    return len(pq)
