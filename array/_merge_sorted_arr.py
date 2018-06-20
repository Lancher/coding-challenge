# LEETCODE@ 88. Merge Sorted Array
#
# --END--


def merge(nums1, m, nums2, n):
    for i in range(m - 1, -1, -1):
        nums1[n + i] = nums1[i]

    i, j, k = n, 0, 0
    while i < m + n or j < n:
        if i >= m + n:
            nums1[k] = nums2[j]
            j, k = j + 1, k + 1
        elif j >= n:
            nums1[k] = nums1[i]
            i, k = i + 1, k + 1
        elif nums1[i] < nums2[j]:
            nums1[k] = nums1[i]
            i, k = i + 1, k + 1
        else:
            nums1[k] = nums2[j]
            j, k = j + 1, k + 1
