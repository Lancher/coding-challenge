# LEETCODE@ 32. Longest Valid Parentheses
#
# --END--


def longestValidParentheses(self, s):
    if not s:
        return 0

    n = len(s)
    # 1) dp[] is defined as number of longest parentheses end at here
    dp = [0] * n

    for i in range(n):
        if s[i] == ')':
            # 2) when we declare new index, we must check the index exist
            if 0 <= i - 1:
                # 3) find corresponding pair "(", "(.....)"
                pair_i = i - dp[i - 1] - 1
                if 0 <= pair_i:
                    if s[pair_i] == '(':
                        # 4) the situation might happen "()(.....)", so we have to take a look a step forward
                        concat = dp[pair_i - 1] if 0 <= pair_i - 1 else 0
                        dp[i] = max(dp[i], concat + i - pair_i + 1)
    return max(dp)
