

# 一个sorted integer array, 除了一个特例以外其他相邻的数字都是相同的（e.g. [1,1,2,3,3,4,4,7,7]）
# 要求找出那个没有被重复的数字，先说了一个O(N)的解法后来写了个logn的binary search。


def binary_search_find_single_num(nums):
    # init
    n = len(nums)
    lo, hi = 0, n - 1

    # do binary search
    while lo < hi:
        mi = (lo + hi) // 2
        # [1, 1, 2]
        # [1, 2, 2]
        # [1, 1, 2, 2, 3]
        # [1, 2, 2, 3, 3]
        if mi % 2:
            if nums[mi] != nums[mi+1]:
                lo = mi + 1
            else:
                hi = mi
        else:
            if nums[mi] == nums[mi+1]:
                lo = mi + 1
            else:
                hi = mi

    # return ans
    return nums[lo]


print(binary_search_find_single_num([1, 1, 2]))
print(binary_search_find_single_num([1, 2, 2]))
print(binary_search_find_single_num([1, 1, 2, 2, 3]))
print(binary_search_find_single_num([1, 2, 2, 3, 3]))


# given array, please find the first index where array[index] > target x


def find_first_num_greater_than_k(nums, k):
    # validate
    if not nums or nums[-1] <= k:
        return -1

    # init
    n = len(nums)
    lo, hi = 0, n - 1

    # do binary search
    while lo < hi:
        mi = (lo + hi) // 2
        # [3, 5], k = 4
        # [4, 5], k = 4
        # [5, 5], k = 4
        if nums[mi] <= k:
            lo = mi + 1
        else:
            hi = lo
    return lo


print(find_first_num_greater_than_k([3, 5], 4))
print(find_first_num_greater_than_k([4, 5], 4))
print(find_first_num_greater_than_k([5, 5], 4))
print(find_first_num_greater_than_k([3], 4))
print(find_first_num_greater_than_k([], 4))




