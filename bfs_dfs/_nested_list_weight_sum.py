# LEETCODE@ 339. Nested List Weight Sum
#
# --END--


def depth_sum_bfs(nestedList):
    res = 0
    dep = 1
    q = nestedList

    while q:
        next_q = []
        for ni in q:
            if ni.isInteger():
                res += ni.getInteger() * dep
            else:
                next_q += ni.getList()
        dep += 1
        q = next_q
    return res


def depth_sum_dfs(nestedList):
    res = 0
    stack = [[nestedList, 0]]
    while stack:
        l, i = stack[-1]
        if i == len(l):
            stack.pop()
        else:
            if l[i].isInteger():
                res += l[i].getInteger() * len(stack)
                stack[-1][1] += 1
            else:
                stack[-1][1] += 1
                stack.append([l[i].getList(), 0])
    return res
