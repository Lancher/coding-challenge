# LEETCODE@ 84. Largest Rectangle in Histogram
#
# 1. Example:
#
#               [ ]
#               [ ][ ]
#         [ ]   [ ][ ]
#       _ [ ][ ][ ][ ] _
#
#   In our stack, we have to maintain increasing order in our stack.
#
#               [ ]
#            [ ][ ]
#            [ ][ ]
#       _ [ ][ ][ ] _
#
# 2. When we face this problem of keep increasing order, we only store idx in the stack.
#
# --END--


def largestRectangleArea(self, heights):
    stack = []
    res = 0

    # keep increasing order in stack
    for j in range(len(heights)):
        while stack and heights[j] < heights[stack[-1]]:
            h_idx = stack.pop()
            i = stack[-1] if stack else -1
            res = max(res, heights[h_idx] * (j - i - 1))
        stack.append(j)

    # clear the rest of stack
    while stack:
        h_idx = stack.pop()
        i = stack[-1] if stack else -1
        res = max(res, heights[h_idx] * (len(heights) - i - 1))

    return res


def largest_rectangle_area_in_histogram(heights):
    heights.append(0)
    stack = [-1]
    res = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            idx = stack.pop()
            area = heights[idx] * (i - stack[-1] - 1)
            res = max(res, area)
        stack.append(i)
    return res


# LEETCODE@ 85. Maximal Rectangle
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
def maximal_rectangle(self, matrix):
    if not matrix or not matrix[0]:
        return 0

    largest = 0
    n = len(matrix[0])
    heights = [0] * (n + 1)

    for row in matrix:
        # accumulate the height from the top to down
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0

        stack = [-1]
        for i in range(n + 1):
            while heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                area = heights[idx] * (i - stack[-1] - 1)
                largest = largest if largest > area else area
            stack.append(i)

    return largest
