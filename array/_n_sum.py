# LEETCODE@ 1. Two Sum
#
# Solution: hash table
#
# --END--


def two_sum(nums, target):
    d = {}
    for i in range(len(nums)):
        j = target - nums[i]
        if j in d:
            return [d[j], i]
        d[nums[i]] = i


# LEETCODE@ 167. Two Sum II - Input array is sorted
#
# Solution: two pointers
#
# --END


def two_sum_with_sorted_array(nums, target):
    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return [i + 1, j + 1]
        elif s < target:
            i += 1
        else:
            j -= 1
    return [-1, -1]


# LEETCODE@ 170. Two Sum III - Data structure design
#
# Solution: hashtable
#
# -END


class TwoSum(object):
    def __init__(self):
        self._map = {}

    def add(self, number):
        if number not in self._map:
            self._map[number] = 0
        self._map[number] += 1

    def find(self, value):
        for number in self._map.keys():
            pair_number = value - number
            if number == pair_number:
                if self._map[number] >= 2:
                    return True
            else:
                if pair_number in self._map:
                    return True
        return False


# LEETCODE@ 15. 3Sum
#
# Solution: 3 pointers
#
# --END--


def three_sum(nums):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if nums[i] + nums[i+1] + nums[i+2] > 0:
            break
        if nums[i] + nums[len(nums)-2] + nums[len(nums)-1] < 0:
            continue
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            tmp = nums[i] + nums[j] + nums[k]
            if tmp == 0:
                result.append([nums[i], nums[j], nums[k]])
                while j + 1 < k and nums[j+1] == nums[j]:
                    j += 1
                j += 1
                while k - 1 > j and nums[k-1] == nums[k]:
                    k -= 1
                k -= 1
            elif tmp < 0:
                # we do not need while loop here
                j += 1
            else:
                # we do not need while loop here
                k -= 1
    return result


# LEETCODE@ 16. 3Sum Closest
#
# Solution: 3 pointers
#
# The time complexity is O(n^2).
#
# --END--
def three_sum_closest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                return s
            elif s > target:
                if s - target < abs(res - target):
                    res = s
                k -= 1
            else:
                if target - s < abs(res - target):
                    res = s
                j += 1
    return res


# LEETCODE@ 259. 3Sum Smaller
#
# --END


def threeSumSmaller(self, nums, target):
    if not nums:
        return 0

    nums.sort()

    cnt = 0
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        k = len(nums) - 1

        while j < k:
            if nums[i] + nums[j] + nums[k] < target:
                cnt += k - j
                j += 1
            else:
                k -= 1
        i += 1
    return cnt


# LEETCODE@ 18. 4Sum
#
# --END


def four_sum(nums, target):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 3):
        if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            break
        if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
            continue
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, n - 2):
            if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                break
            if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                continue
            if j != i + 1 and nums[j] == nums[j-1]:
                continue
            k, l = j + 1, n - 1
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                if s == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    while k + 1 < l and nums[k] == nums[k+1]:
                        k += 1
                    k += 1
                    while l - 1 > k and nums[l] == nums[l-1]:
                        l -= 1
                    l -= 1
                elif s < target:
                    k += 1
                else:
                    l -= 1
    return res

