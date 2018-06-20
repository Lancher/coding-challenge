# LEETCODE@ 223. Rectangle Area
#
# 1. if two line overlaps,
#
#    A ------------ B
#
#             c ----------------D
#
#   => B < C && A < D
#
#             A ------------ B
#
#   c ----------------D
#
#   => B < C && A < D
#
# --END--


def computeArea(A, B, C, D, E, F, G, H):
    duplicate = 0
    if A < G and E < C and B < H and F < D:
        xs = sorted([A, G, E, C])
        ys = sorted([B, H, F, D])
        duplicate = (xs[2] - xs[1]) * (ys[2] - ys[1])
    return (C - A) * (D - B) + (G - E) * (H - F) - duplicate

