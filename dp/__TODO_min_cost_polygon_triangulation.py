# http://www.geeksforgeeks.org/minimum-cost-polygon-triangulation/
import math


def dst(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))


def cost(points, i, j, k):
    return dst(points[i], points[j]) + dst(points[j], points[k]) + dst(points[i], points[k])


# recursive take 2^n
def min_cost_polygon_recursive(points, i, j):
    if j - i < 2:
        return 0

    res = 1000
    for k in range(i + 1, j):
        res = min(
            res,
            min_cost_polygon_recursive(points, i, k) +
            min_cost_polygon_recursive(points, k, j) +
            cost(points, i, j, k)
        )
    return res


points = [(0, 0), (1, 0), (2, 1), (1, 2), (0, 2)]
print(min_cost_polygon_recursive(points, 0, len(points) - 1))


# dp, time complexity is O(n^3)
def min_cost_polygon_iterative(points):
    if len(points) < 3:
        return 0

    n = len(points)
    dp = [[1000 for j in range(n)] for i in range(n)]

    # length
    for l in range(1, n + 1):
        # i, j => start, end points
        i, j = 0, l - 1
        while j < n:
            # same points or adjacent points
            if j - i < 2:
                dp[i][j] = 0
            # k is the slice point
            else:
                for k in range(i + 1, j):
                    m = dp[i][k] + dp[k][j] + cost(points, i, j, k)
                    if m < dp[i][j]:
                        dp[i][j] = m

            i, j = i + 1, j + 1

    # our answer
    return dp[0][n-1]


points = [(0, 0), (1, 0), (2, 1), (1, 2), (0, 2)]
print(min_cost_polygon_iterative(points))

