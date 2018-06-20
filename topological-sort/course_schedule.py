

# LEETCODE@ 207. Course Schedule
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
def canFinish(self, numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    visited = [0] * numCourses
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])

    # 0: unvisited, 1: visiting, 2: visited
    def dfs(i):
        if visited[i] == 0:
            visited[i] = 1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 2
            return True
        elif visited[i] == 1:
            return False
        else:
            return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True


# LEETCODE@ 210. Course Schedule II
#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
def findOrder(self, numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    visited = [0] * numCourses
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
    res = []

    def dfs(i):
        if visited[i] == 0:
            visited[i] = 1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 2
            res.append(i)
            return True
        elif visited[i] == 1:
            return False
        else:
            return True

    for i in range(numCourses):
        if not dfs(i):
            return []
    return res[::-1]
