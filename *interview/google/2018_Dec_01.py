

# 第一轮：给一个array，每个elem表示硬币的数量。两个人每次只能拿index数量的硬币，交替拿，
# 假如到player1的时候没有办法从任意一个位置拿硬币了，那么player1输。问第一个player是否可以赢。
#
# 每个index上能拿的次数不就是 num/i 吗，这样总共能拿的次数就确定了，player1输赢一开始就确定了，
# player1有什么办法能改变命运吗？
def can_player1_win(coins):
    cnt = 0
    for i in range(1, len(coins)):
        cnt += coins[i] // i
    return cnt % 2 == 1


print(can_player1_win([0, 2, 3, 4]))


# 第二问：有一个combine function，可以把两个相邻位置的硬币combine，最后成为一个只有一个elem的
# array，所需要的cost是这两个位置的硬币的数量之和，比如说：[0]1, [1]2, [2]3 combine[0][1]，那么
# 所需要的cost就是3，这个时候的数组就变成[0]3, [1]3。问所需最少cost可以最后变成一个elem的array。
def min_cost_combine_coins(coins):
    # build dp array
    n = len(coins)
    dp = [[0 for j in range(n)] for i in range(n)]

    #   dp coin      dp cost
    #  1   3   6    0  3  min(3, 5) + 6
    #      2   5       0  5
    #          3          0
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + sum(coins[i:j+1])

    return dp[0][n-1]


print('min cost to combine coins:', min_cost_combine_coins([1, 2, 3]))


# 第二轮：有一个celling，从上面延伸下来很多brick，这些brick只有在跟有celling连接的brick相邻才可以
# 不掉下来。问remove掉一个brick，会跌下来的brick的数量。
# LeetCode

class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def root(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_p, root_q = self.root(p), self.root(q)
        if root_p != root_q:
            if self.size[root_p] < self.size[root_q]:
                self.parent[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.parent[root_q] = root_p
                self.size[root_p] += self.size[root_q]


class Solution:
    def hitBricks(self, grid: 'List[List[int]]', hits: 'List[List[int]]') -> 'List[int]':
        # init
        m, n = len(grid), len(grid[0])

        # set the hitting bricks from 1 to 2
        for i, j in hits:
            if grid[i][j] == 1:
                grid[i][j] = 2

        # union, let the first row connect to `m * n`
        un = Union(m * n + 1)
        for j in range(n):
            if grid[0][j] == 1:
                un.union(m * n, j)

        # union the rest of rows
        for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + x, j + y
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            un.union(i * n + j, ni * n + nj)

        # hits
        ln = len(hits)
        res = [0] * ln
        for k in range(ln - 1, -1, -1):
            i, j = hits[k][0], hits[k][1]
            if grid[i][j] == 2:
                pre_size = un.size[un.root(m * n)]
                grid[i][j] = 1
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        un.union(i * n + j, ni * n + nj)

                # i == 0, we need to union with ceil m * n
                if i == 0:
                    un.union(i * n + j, m * n)
                cur_size = un.size[un.root(m * n)]
                res[k] = max(0, cur_size - pre_size - 1)
        return res


# TODO: 第三轮：给一个array，里面的数字可以用任意+-*/()连接，然后问最后的结果的数量。注意顺序不可以变。


# TODO: 第四轮：给一个graph，用map表示，保证是一个ring，问如何返回一个clockwise or counter-clockwise的
# TODO: node的数组。这道题目主要考察的是test input。比如map是{1:[2,2], 2:[1,1]}这种。


# 1. 白人，迟到了半个小时，貌似是临时重新安排了一个？
# 给一个list，找出多少种split 的方法，比如 [1,2,3,4,4] -> [1,2,3] + [4] + [4], 或者 [1,2,3,4,4]-> [1,2,3] + [4,4] etc... 血崩
import collections


def num_of_splits(nums):
    # build combinations
    n = len(nums)
    arr, combs = [], []
    comb_sum(1, n, arr, 0, combs)

    # build factorial cache
    fact = [i for i in range(n + 1)]
    fact[0] = 1
    for i in range(1, n + 1):
        fact[i] *= fact[i-1]

    # count combinations
    res = 0
    for comb in combs:
        counter = collections.Counter(comb)

        # 3! / (2! * 1!)
        num = fact[len(comb)]
        for _, cnt in counter.items():
            num //= fact[cnt]
        res += num
    return res


def comb_sum(nxt_i, n, arr, sm, res):
    if sm == n:
        res.append(arr[:])

    for i in range(nxt_i, n + 1):
        if i + sm <= n:
            arr.append(i)
            comb_sum(i, n, arr, sm + i, res)
            arr.pop()


print('number of ways to split array:', num_of_splits([1, 2, 3]))


# 2. 亚洲人大叔？
# 找一堆数的的median，数的范围是0-1000，bucket sort。
# 很复杂的context，转换成了一个复杂的有很多condition的binary search做？不太记得了，但应该不难
def find_median_with_range(nums):
    # init
    n = len(nums)
    bucket = [0] * 1001

    # put into bucket
    for num in nums:
        bucket[num] += 1

    # find [0, 1, 2, 3]
    #      pre mi
    pre_mi, mi = -1, -1
    sm = 0
    for i in range(1001):
        sm += bucket[i]
        if pre_mi == - 1 and n // 2 <= sm:
            pre_mi = i
        if mi == - 1 and n // 2 + 1 <= sm:
            mi = i

    print(pre_mi, mi)
    if n % 2 == 1:
        return mi
    else:
        return (pre_mi + mi) / 2


print('find median', find_median_with_range([1, 1, 2, 2, 3, 3]))
print('find median', find_median_with_range([10, 5]))


# 3. 国人小姐姐
# 转汇率那道，说可以用dfs和union find做，她表示随便选哪种，选了union find，在纸上写就改得乱七八糟了。


def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    # build a graph
    graph = collections.defaultdict(dict)
    for eq, val in zip(equations, values):
        graph[eq[0]][eq[0]] = 1.0
        graph[eq[1]][eq[1]] = 1.0
        graph[eq[0]][eq[1]] = val
        graph[eq[1]][eq[0]] = 1 / val

    # run BFS for each query
    res = [-1.0] * len(queries)
    for i in range(len(queries)):
        st, ed = queries[i][0], queries[i][1]

        # 'x' might not in it
        if st not in graph or ed not in graph:
            continue

        # bfs
        queue = [(st, 1.0)]
        vst = set([st])
        while queue:
            nxt_queue = []
            for node, val in queue:
                if node == ed:
                    res[i] = val
                    nxt_queue = []
                    break

                # nxt_node is not visited
                for nxt_node in graph[node]:
                    if nxt_node not in vst:
                        nxt_queue.append((nxt_node, val * graph[node][nxt_node]))
                        vst.add(nxt_node)
            queue = nxt_queue
    return res

equations = [ ["a","b"],["b","c"] ]
values = [2.0,3.0]
queries = [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"]]
print('equations', calcEquation(equations, values, queries))


# 国人大哥-baidu 1point3acres
# 一个array，就问能不能把它split成多个顺子，比如3,4,5,6,7和4,5,6,7,8,9,10等等等


import heapq


def isPossible(nums: 'List[int]') -> 'bool':
    end_heap = {}

    # iterate the numbers
    for i, num in enumerate(nums):
        # we connect with previous value
        pre = num - 1
        if pre in end_heap:
            # pop the shortest length
            ln = heapq.heappop(end_heap[pre])
            if len(end_heap[pre]) == 0:
                end_heap.pop(pre)

            # append to new ending
            ln += 1
            if num not in end_heap:
                end_heap[num] = []
            heapq.heappush(end_heap[num], ln)
        else:
            ln = 1
            if num not in end_heap:
                end_heap[num] = []
            heapq.heappush(end_heap[num], ln)

    for end, hp in end_heap.items():
        for ln in hp:
            if ln < 3:
                return False
    return True


print('is possible', isPossible([1,2,3,3,4,4,5,5]))
