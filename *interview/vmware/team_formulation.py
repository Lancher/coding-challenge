import time


def team_formulation(nums, lo, hi, k):
    nums = [num for num in nums if lo <= num <= hi]
    nums.sort()

    tmp, res = [], [0]
    backtracing(nums, 0, k, tmp, res)
    return res[0]


def backtracing(nums, nxt_i, k, tmp, res):
    if k <= len(tmp):
        res[0] += 1
    for i in range(nxt_i, len(nums)):
        if i != nxt_i and nums[i] == nums[i-1]:
            continue
        tmp.append(nums[i])
        backtracing(nums, i + 1, k, tmp, res)
        tmp.pop()


nums = [12, 4, 6, 13, 5, 10, 12, 4, 6, 13, 5, 10, 12, 4, 6, 13, 5, 10, 12, 4, 6, 13, 5, 10]
nums1 = [7, 7, 7, 7, 7, 7]

st = time.time()
print(team_formulation(nums, 0, 20, 3))
ed = time.time()
print(ed - st)

