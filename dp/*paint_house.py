# LEETCODE@ 256. Paint House
#
# --END--


def minCost(self, costs):
    # 1) Remember the empty costs.
    if not costs:
        return 0

    r, b, g = costs[0][0], costs[0][1], costs[0][2]
    for i in range(1, len(costs)):
        r, b, g = costs[i][0] + min(b, g), costs[i][1] + min(r, g), costs[i][2] + min(r, b)
    return min(r, b, g)


# LEETCODE@ 265. Paint House II
#
# --END--


def minCostII(self, costs):
    if not costs or not costs[0]:
        return 0
    m, n = len(costs), len(costs[0])

    # 1) dp initialization
    m1, m2 = -1, -1
    for j in range(n):
        if m1 == -1 or costs[0][j] < costs[0][m1]:
            m1, m2 = j, m1
        elif m2 == -1 or costs[0][j] < costs[0][m2]:
            m2 = j

    for i in range(1, m):
        pre_m1, pre_m2 = m1, m2
        m1, m2 = -1, -1

        # 2) count the current costs
        for j in range(n):
            if pre_m1 == j:
                costs[i][j] += costs[i - 1][pre_m2]
            else:
                costs[i][j] += costs[i - 1][pre_m1]

            # 3) update m1, m2
            if m1 == -1 or costs[i][j] < costs[i][m1]:
                m1, m2 = j, m1
            elif m2 == -1 or costs[i][j] < costs[i][m2]:
                m2 = j

    return costs[m - 1][m1]