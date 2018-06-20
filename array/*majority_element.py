# LEETCODE@ 169. Majority Element
#
# 1. https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
#
# 2. Example:
#
#   [2, 100, 2, 2, -1, 2, 3]
#
#   We can think the array as
#
#   [2, x, 2, 2, x, 2, x]
#
#   keep counting and the the majority will be the last one.
#
# --END--


def find_majority(nums):
    cnt = 1
    res = nums[0]

    for i in range(1, len(nums)):
        if res == nums[i]:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            res, cnt = nums[i], 1
    return res


# LEETCODE@ 229. Majority Element II
#
# 1. The question is like  `Majority Element`.
#
# --END--


def find_majority_2(nums):
    if not nums:
        return []

    cnt1, cnt2, cand1, cand2 = 0, 0, -1, -1
    for num in nums:
        if num == cand1:
            cnt1 += 1
        elif num == cand2:
            cnt2 += 1
        elif cnt1 == 0:
            cnt1, cand1 = 1, num
        elif cnt2 == 0:
            cnt2, cand2 = 1, num
        else:
            cnt1, cnt2 = cnt1 - 1, cnt2 - 1

    return [cand for cand in [cand1, cand2] if nums.count(cand) > len(nums) / 3]
