
def find_overlapping_time(intervals):
    if not intervals:
        return []

    results = []

    intervals.sort(key=lambda o: o[0])

    cur_st, cur_ed = intervals[0]

    for i in range(1, len(intervals)):
        st, ed = intervals[i]
        if st <= cur_ed:
            cur_ed = max(cur_ed, ed)
        else:
            results.append([cur_st, cur_ed])
            cur_st, cur_ed = st, ed
    results.append([cur_st, cur_ed])
    return results

assert find_overlapping_time([[7, 7], [2, 3], [6, 11], [1, 2]]) == [[1, 3], [6, 11]]
