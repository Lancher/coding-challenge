# LEETCODE@ 768 & LEETCODE@ 769. Max Chunks to Make Sorted (ver. 2)
#
# 1. How to slice the array ?
#
#    [1, 0, 2, 3, 4]
#
#          |  |  |   => there are 3 slices and 4 sub arrays
#
# 2. The array can be sliced only when left part maximum <= right part minimum
#
#    [1, 0] [2, 3, 4]
#    [1, 0, 2] [3, 4]
#    [1, 0, 2, 3] [4]
#
# 3. Build the left maximum array & right minimum array:
#
#    [1, 1, 2, 3, 4]
#
#       |              ==> Take left part from above and right part below to determine whether slice happen
#
#    [0, 0, 2, 3, 4]
#
# --END--


def maxChunksToSorted(self, arr):
    left_max = arr[:]
    right_min = arr[:]

    for i in range(1, len(arr)):
        left_max[i] = max(left_max[i - 1], arr[i])

    for i in range(len(arr) - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], arr[i])

    res = 0
    for i in range(len(arr) - 1):
        if left_max[i] <= right_min[i + 1]:
            res += 1
    return res + 1
