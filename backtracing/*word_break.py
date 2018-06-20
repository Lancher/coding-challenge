# LEETCODE@ 139. Word Break
#
# --END--


def wordBreak(self, s, wordDict):
    n = len(s)
    st = set()

    # use string length as dp array, and remember empty string d[0] is True.
    # dp[i] means that s[0:i] can be partition to single or multiple elements in linkedinlist.
    dp = [0] * (n + 1)
    dp[0] = 1

    for w in wordDict:
        st.add(w)

    for j in range(1, n + 1):
        for i in range(j):
            if dp[i] and s[i:j] in st:
                dp[j] = 1
                break
    return bool(dp[-1])


# LEETCODE@ 140. Word Break II
#
# 1. DP do the trick to eliminate impossible possibility.
#
#   cat | sanddog
#
#   When we cut the `cat`, we know if the rest string `sanddog` be be cut, the length of result
#   will increment.
#
#   DP[i] = 1 means that from i to the end can be partition.
#
#
# --END--

def wordBreak(self, s, wordDict):
    st = set()
    for w in wordDict:
        st.add(w)
    # the default value of DP is 1, we will later change to 0
    l, res, dp = [], [], [1] * (len(s) + 1)
    self.backtracing(s, st, 0, dp, l, res)
    return res


def backtracing(self, s, st, i, dp, l, res):
    if i == len(s):
        res.append(' '.join(l[:]))
    else:
        for j in range(i + 1, len(s) + 1):
            tmp = s[i:j]
            if dp[j] and tmp in st:
                l.append(tmp)
                sz = len(res)
                self.backtracing(s, st, j, dp, l, res)
                # check if s[j:] can be partitioned
                if sz == len(res):
                    dp[j] = 0
                l.pop()
