# LEETCODE@ 56. Merge Intervals
#
# --END--


def merge(intervals):
    if not intervals:
        return []
    res = []
    intervals.sort(key=lambda i: i.start)

    new_i = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i].start <= new_i.end:
            new_i.end = max(intervals[i].end, new_i.end)
        else:
            res.append(new_i)
            new_i = intervals[i]
    res.append(new_i)
    return res
