# LEETCODE@ 78. Subsets
#
# --END--


def subsets(self, nums):
    l, res = [], []
    self.backtracing(nums, 0, l, res)
    return res


def backtracing(self, nums, s, l, res):
    res.append(l[:])

    for i in range(s, len(nums)):
        l.append(nums[i])
        self.backtracing(nums, i + 1, l, res)
        l.pop()


# LEETCODE@ 90. Subsets II
#
# --END--


def subsetsWithDup(self, nums):
    nums.sort()
    l = []
    result = []
    self.backtrace(nums, result, l, 0)
    return result


def backtrace(self, nums, result, l, s):
    result.append(l[:])

    for i in range(s, len(nums)):
        if i > s and nums[i] == nums[i-1]:
            continue
        l.append(nums[i])
        self.backtrace(nums, result, l, i + 1)
        l.pop()
