# LEETCODE@ 797. All Paths From Source to Target
#
# Solution 1: BFS
#
# Solution 2: DFS with backtracing is less memory
#
# --END--


import collections


class Solution:
    def allPathsSourceTarget(self, graph):

        res = []
        n = len(graph)
        # always put the finished state
        q = [[0, [0]]]

        while q:
            next_q = []
            for i, l in q:
                if i == n - 1:
                    res.append(l[:])
                else:
                    for j in graph[i]:
                        next_q.append([j, l[:] + [j]])
            q = next_q

        return res
