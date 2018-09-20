# LEETCODE 853. Car Fleet
#
# --END00


def carFleet(self, target, pos, speed):
    time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
    res = cur = 0
    for t in time[::-1]:
        if t > cur:
            res += 1
            cur = t
    return res