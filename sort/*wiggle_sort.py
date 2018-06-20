# LEETCODE@ 280. Wiggle Sort
#
# 1) There are only 4 possible cases:
#
#   1. a <= b <= c --> swap(b, c)
#   2. a <= b >= c --> done
#   3. a >= b <= c --> swap(a, b), then it could be either case 1 or 2
#   4. a >= b >= c --> swap(a, b)
#
# --END--


def wiggleSort(self, nums):
    if len(nums) < 2:
        return

    for i in range(1, len(nums), 2):
        if nums[i - 1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
        if i + 1 < len(nums) and nums[i + 1] > nums[i]:
            nums[i + 1], nums[i] = nums[i], nums[i + 1]
