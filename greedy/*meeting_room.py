# LEETCODE@ 252. Meeting Rooms
#
# --END--


def canAttendMeetings(self, intervals):
    n = len(intervals)
    intervals.sort(key=lambda o: o.start)

    for i in range(n - 1):
        if intervals[i + 1].start < intervals[i].end:
            return False
    return True


# LEETCODE@ 253. Meeting Rooms II
#
# Given an array of meeting time intervals consisting of start and end times
import heapq


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def minMeetingRooms(self, intervals):
    n = len(intervals)
    h = []

    # 1) sort by start
    intervals.sort(key=lambda o: o.start)

    # 2) greedy to keep pushing the rooms
    for i in range(n):
        if not h or h[0][1].end > intervals[i].start:
            heapq.heappush(h, [intervals[i].end, intervals[i]])
        else:
            heapq.heapreplace(h, [intervals[i].end, intervals[i]])

    return len(h)
