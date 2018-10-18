# LEETCODE@ 31. Next Permutation
#
# 1. Example:
#
#   [2, 3, 6, 5, 4, 1]
#
#   1) From right to left, find the first item not in increasing order.We find 3.
#
#   2) From right to left, find the first item greater than 3. We find 4.
#
#   3) Swap 3 and 4.
#
#   4) Reverse value after 4.
#
# --END--


def nextPermutation(self, nums):
    # Step 1
    i = len(nums) - 2
    while i > -1 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        self.reverse(nums, 0, len(nums) - 1)
        return
    # Step 2
    j = len(nums) - 1
    while j >= i and nums[j] <= nums[i]:
        j -= 1
    # Step 3
    nums[i], nums[j] = nums[j], nums[i]
    # Step 4
    self.reverse(nums, i + 1, len(nums) - 1)


def reverse(self, nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1


# LEETCODE@ 46. Permutations
#
# [1,2,3] have the following permutations:
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
# --END--


def permute(self, nums):
    used = [0] * len(nums)
    l, res = [], []
    self.backtracing(nums, used, l, res)
    return res


def backtracing(self, nums, used, l, res):
    if len(l) == len(nums):
        res.append(l[:])
    else:
        for i in range(len(nums)):
            if not used[i]:
                l.append(nums[i])
                used[i] = 1
                self.backtracing(nums, used, l, res)
                l.pop()
                used[i] = 0


# LEETCODE@ 47. Permutations II
#
# --END--


def permuteUnique(self, nums):
    used = [0] * len(nums)
    l, res = [], []
    nums.sort()
    self.backtracing(nums, used, l, res)
    return res


def backtracing(self, nums, used, l, res):
    if len(l) == len(nums):
        res.append(l[:])
    else:
        # To avoid duplicate items, we will not use the same element in the same loop.
        pre_num = None
        for i in range(len(nums)):
            if not used[i] and nums[i] != pre_num:
                pre_num = nums[i]
                l.append(nums[i])
                used[i] = 1
                self.backtracing(nums, used, l, res)
                l.pop()
                used[i] = 0


# LEETCODE@ 60. Permutation Sequence
#
# --END--


def getPermutation(self, n, k):
    l = [str(i) for i in range(1, n + 1)]
    groups = n
    items = math.factorial(n)
    ans = ''
    k -= 1

    while groups:
        items /= groups
        i, k = k / items, k % items
        ans += l[i]
        l.pop(i)
        groups -= 1

    return ans
