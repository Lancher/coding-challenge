# LEETCODE@ 657. Judge Route Circle
#
# --END--


def judgeCircle(self, moves):
    v, h = 0, 0
    for m in moves:
        if m == 'U':
            v += 1
        elif m == 'D':
            v -= 1
        elif m == 'L':
            h -= 1
        else:
            h += 1
    return v == 0 and h == 0