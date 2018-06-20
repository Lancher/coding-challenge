# LEETCODE@ 96. Unique Binary Search Trees
#
# --END--


def unique_of_bst(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            # if j = 1, one node behind 1 and i-1-1 node after j
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]


# LEETCODE@ 95. Unique Binary Search Trees II
#
# 1. Backtracing
#
# --END--


def unique_of_bst_2(n):
    if n == 0:
        return []
    return build(1, n)


def build(lo, hi):
    if lo > hi:
        return [None]
    elif lo == hi:
        return [Node(lo)]
    else:
        res = []
        for i in range(lo, hi + 1):
            l_nodes = build(lo, i - 1)
            r_nodes = build(i + 1, hi)

            for l_node in l_nodes:
                for r_node in r_nodes:
                    node = Node(i)
                    node.left = l_node
                    node.right = r_node
                    res.append(node)
        return res

