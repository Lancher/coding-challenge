# https://github.com/perixtar/2024-Tech-OA?tab=readme-ov-file
import collections


def find_min_trips(ws):
    trips = 0

    w_cnt = collections.defaultdict(int)
    for w in ws:
        w_cnt[w] += 1

    for cnt in w_cnt.values():
        if cnt == 1:
            return -1
        elif cnt % 3 == 0:
            trips += cnt // 3
        else:
            trips += cnt // 3 + 1

    return trips


assert find_min_trips([1, 8, 5, 8, 5, 1, 1]) == 3
assert find_min_trips([3, 4, 4, 3, 1]) == -1
assert find_min_trips([2, 4, 6, 6, 4, 2, 4]) == 3