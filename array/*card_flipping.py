# LEETCODE@ 822. Card Flipping Game
#
# 1) it is very tricky
#
# --END--


def flipgame(self, fronts, backs):
    n = len(fronts)
    # 1) out possible answers
    st = set(fronts + backs)

    # 2) run through and then check if `num == fronts[i] == backs[i]`.
    for num in st:
        for i in range(n):
            # 3) the number is not good
            if num == fronts[i] == backs[i]:
                break
        else:
            return num
    return 0
