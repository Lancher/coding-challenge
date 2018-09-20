# LEETCODE@ 638. Shopping Offers
#
# 1. The idea is very similar to combination sum.
#
# --END--


def shoppingOffers(self, price, special, needs):
    return self.helper(price, special, needs, 0)


def helper(self, price, special, needs, nxt_i):
    mn = self.direct_buy(price, needs)

    for i in range(nxt_i, len(special)):
        # check if this special offer can be applied
        nxt_needs = [0] * len(needs)
        for j in range(len(special[i]) - 1):
            if needs[j] < special[i][j]:
                nxt_needs = None
                break
            else:
                nxt_needs[j] = needs[j] - special[i][j]

        # if the special can be applied
        if nxt_needs:
            mn = min(mn, special[i][-1] + self.helper(price, special, nxt_needs, i))

    return mn


def direct_buy(self, price, needs):
    res = 0
    for i in range(len(price)):
        res += price[i] * needs[i]
    return res
