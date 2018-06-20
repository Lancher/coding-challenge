# LEETCODE@ 780. Reaching Points
#
# 1. GCD to approach the start point from the END point.
#
# --END--


def reachingPoints(self, sx, sy, tx, ty):
    # 1) like GCD
    while sx < tx and sy < ty:
        if tx < ty:
            ty = ty % tx
        else:
            tx = tx % ty

    # 2) last checking
    return sx == tx and (ty - sy) % tx == 0 or sy == ty and (tx - sx) % ty == 0
