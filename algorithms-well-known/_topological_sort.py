# 1. DFS so the cycles is not allowed
#
# 2. length of graph is the number of nodes
#
# 3. Example:
#
#   0 --> 2 --> 3 --> 4
#         ^
#   1 --- |
#
#   Node 4 and his children will be done and append to array
#   Node 3 and his children will be done and append to array
#   Node 2 and his children will be done and append to array
#   Node 0 and his children will be done and append to array
#   Node 1 and his children will be done and append to array
#   [4, 3, 2, 0, 1] reverse [1, 0, 2, 3, 4]
#
#
# --END--


def topological_sort(g):
    visited = [0] * len(g)
    res = []

    # inner function can only reference the mutable outer variables
    def dfs(u):
        if not visited[u]:
            visited[u] = 1
            for v in g[u]:
                dfs(v)

            # when all children are done, we append current node
            res.append(u)

    # run DFS
    for u in range(len(g)):
        dfs(u)

    # return reverse order
    return res[::-1]


g = {0: [2], 1: [2], 2: [3], 3: [4], 4: []}
print(topological_sort(g))
