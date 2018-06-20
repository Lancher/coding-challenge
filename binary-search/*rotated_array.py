# LEETCODE@ 153. Find Minimum in Rotated Sorted Array
#
# --END--


def find_min(nums):
    n = len(nums)
    lo, hi = 0, n - 1

    while lo < hi:
        mi = int((lo + hi) / 2)
        if nums[mi] < nums[n - 1]:
            hi = mi
        else:
            lo = mi + 1
    return nums[lo]


# LEETCODE@ 154. Find Minimum in Rotated Sorted Array II
#
# --END--


def find_min_with_dup(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mi = (lo + hi) / 2
        #
        if nums[mi] == nums[hi]:
            hi -= 1
        elif nums[mi] <= nums[hi]:
            hi = mi
        else:
            lo = mi + 1
    return nums[lo]


# LEETCODE@ 33. Search in Rotated Sorted Array
#
# --END--


def search(self, nums, target):
    n = len(nums)
    lo, hi = 0, n - 1

    # 1) always use lo < hi
    # 2) if the element cannot be found, we just check at the end
    while lo < hi:
        mi = int((lo + hi) / 2)
        if nums[mi] == target:
            return mi

        # 3) nums[mi] == nums[hi] cannot happen because all the elements are different
        if nums[mi] < nums[hi]:
            if nums[mi] < target <= nums[hi]:
                lo = mi + 1
            else:
                hi = mi
        else:
            if nums[lo] <= target < nums[mi]:
                hi = mi
            else:
                lo = mi + 1

    # 4) empty list
    return lo if lo < len(nums) and nums[lo] == target else -1


# LEETCODE@ 81. Search in Rotated Sorted Array II
#
# --END--


def search(self, nums, target):
    n = len(nums) - 1
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mi = int((lo + hi) / 2)
        if nums[mi] == target:
            return True

        if nums[mi] == nums[hi]:
            val = nums[hi]
            while lo < hi and nums[lo] == val:
                lo += 1
            while lo < hi and nums[hi] == val:
                hi -= 1
        elif nums[mi] < nums[hi]:
            if nums[mi] < target <= nums[hi]:
                lo = mi + 1
            else:
                hi = mi
        else:
            if nums[lo] <= target < nums[mi]:
                hi = mi
            else:
                lo = mi + 1

    # 1) if the element cannot be found, we just check at the end
    return True if lo < len(nums) and nums[lo] == target else False
