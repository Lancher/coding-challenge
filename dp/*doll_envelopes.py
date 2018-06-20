# LEETCODE@ 354. Russian Doll Envelopes
#
# 1) # TODO nlogn solution
#
# 2) dp solution
#
# --END--


def maxEnvelopes(self, envelopes):
    # 1) DP remember the corner case.
    if not envelopes:
        return 0
    dp = [1] * len(envelopes)

    # 2) python 3 sort by key!!!!
    envelopes.sort(key=lambda o: o[0])

    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

