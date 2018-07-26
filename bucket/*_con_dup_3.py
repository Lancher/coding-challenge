# LEETCODE@ 220. Contains Duplicate III
#
# 1) When facing bucket, you have to make sure the size of bucket you want to use.
#
# --END--


def containsNearbyAlmostDuplicate(self, nums, k, t):
    if t < 0:
        return False
    n = len(nums)
    d = {}

    for i in range(n):
        # 1) maintain window size `k+1` [0 1 2 3], k = 3
        if i >= k + 1:
            idx = int(nums[i - k - 1] / (t + 1)) - 1 if nums[i - k - 1] < 0 else int(nums[i - k - 1] / (t + 1))
            d.pop(idx)

        # 2) [0, t] [t+1, 2t+1] [2t+2, 3t+2]
        idx = int(nums[i] / (t + 1)) - 1 if nums[i] < 0 else int(nums[i] / (t + 1))
        if idx in d:
            return True
        if idx - 1 in d and abs(d[idx - 1] - nums[i]) <= t:
            return True
        if idx + 1 in d and abs(d[idx + 1] - nums[i]) <= t:
            return True
        d[idx] = nums[i]
    return False
