# LEETCODE@ 164. Maximum Gap
#
# 1) When dealing with linear sorting, it is bucket sort.
#
# --END--


def maximumGap(self, nums):
    if len(nums) < 2:
        return 0

    # 1) bucket sort is the linear sorting
    n = len(nums)
    mn, mx = min(nums), max(nums)

    # 2) [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5]
    # the minimum of slot should be 1
    w = int((mx - mn) / (n - 1)) + 1

    # 2) put the num into bucket
    sz = int((mx - mn) / w) + 1
    bucket = [[] for i in range(sz)]
    for num in nums:
        bucket[int((num - mn) / w)].append(num)

    # 3) count the max gap
    #   the minimum size of res
    res = int((mx - mn) / (n - 1))
    pre_mx = None
    for b in bucket:
        if b:
            if pre_mx:
                res = max(res, min(b) - pre_mx)
            pre_mx = max(b)
    return res
