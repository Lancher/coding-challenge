# LEETCODE@ 134. Gas Station
#
# 1) If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that
# A can not reach.)
#
# 2) If the total number of gas is bigger than the total number of cost. There must be a solution.
#
# --END--


def canCompleteCircuit(self, gas, cost):
    n = len(gas)
    res = 0
    tank = 0

    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            res = i + 1
            tank = 0
    return -1 if sum(gas) - sum(cost) < 0 else res

