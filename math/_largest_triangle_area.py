# LEETCODE@ 812. Largest Triangle Area
#
# --END--


def largestTriangleArea(self, pts):
    n = len(pts)

    res = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                area = pts[i][0] * (pts[j][1] - pts[k][1]) + pts[j][0] * (pts[k][1] - pts[i][1]) + pts[k][0] * (
                pts[i][1] - pts[j][1])
                area = abs(area) / 2
                res = max(res, area)
    return res
