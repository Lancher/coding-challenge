# LEETCODE@ 802. Find Eventual Safe States
#
# --END--


def eventualSafeNodes(self, graph):
    # 1) set the color
    #   0: unvisited
    #   1: safe
    #   2: unsafe
    n = len(graph)
    vst = [0] * n

    def dfs(v):
        vst[v] = 2
        cnt = 0
        for w in graph[v]:
            # 2) avoid circle
            if not vst[w]:
                dfs(w)
            cnt += vst[w]
        # 3) if all the child are safe, i am safe too.
        if cnt == len(graph[v]):
            vst[v] = 1

    for i in range(n):
        # 4) avoid circle
        if not vst[i]:
            dfs(i)

    res = []
    for i in range(n):
        if vst[i] == 1:
            res.append(i)
    return res
