# LEETCODE@ 540. Single Element in a Sorted Array
#
# --END--


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo , hi = 0, len(nums) - 1

        while lo < hi:
            mi = (lo + hi) // 2
            left_clear = False
            if mi % 2 == 0:
                if nums[mi] == nums[mi+1]:
                    left_clear = True
            else:
                if nums[mi] == nums[mi-1]:
                    left_clear = True
            if left_clear:
                lo = mi + 1
            else:
                hi = mi

        return nums[lo]
