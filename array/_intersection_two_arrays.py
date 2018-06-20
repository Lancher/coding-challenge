# LEETCODE@ 349. Intersection of Two Arrays
#
# --END--


def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


# LEETCODE@ 350. Intersection of Two Arrays II
#
# --END--


def intersect(nums1, nums2):
    res, d1, d2 = [], {}, {}
    for num in nums1:
        if num not in d1:
            d1[num] = 0
        d1[num] += 1
    for num in nums2:
        if num in d1 and d1[num] > 0:
            d1[num] -= 1
            res.append(num)
    return res
