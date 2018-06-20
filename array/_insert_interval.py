# LEETCODE@ 57. Insert Interval
#
# --END--


class Solution(object):
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        l, r = [], []
        for i in intervals:
            if i.end < s:
                l.append(i)
            elif e < i.start:
                r.append(i)
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return l + [Interval(s, e)] + r
