

# def numIslands(self, grid):
#     res = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] == '1':
#                 self.dfs(grid, i, j)
#                 res += 1
#     return res
#
#
# def dfs(self, grid, i, j):
#     grid[i][j] = '0'
#     x, y = 1, 0
#
#     for _ in range(4):
#         x, y = y, -x
#         if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] == '1':
#             self.dfs(grid, i + x, j + y)


# 比较麻烦的followup，就是如果2-D array变成N-D array怎么办
# 关于followup，其实很简单，就是干脆把N-D array里每一个value的index (这个index有N个维度)
# ，写成一个set/list/array/string;
# 比如对于3-D array: [[[1,1], [1,1]], [[2, 2], [2, 2]], [[3, 3], [3, 3]]]
# 那么整个array的第一个"1",表示成 [0, 0, 0], 第二个“1”表示成[0, 0, 1]。。。以此类推。
# 当然要注意每个dimension是有length
# limit的。然后就套用到BFS上去，每个维度在原来基础上index都 + 1 和 -1即可. 1poi

import functools


def numIslands(n, n_arr):
    # build limits of N-D array
    limits = []
    arr = n_arr
    for _ in range(n):
        limits.append(len(arr))
        arr = arr[0]

    def increment_one(point):
        point[-1] += 1
        for i in range(n - 1, -1, -1):
            if point[i] == limits[i]:
                point[i-1] += 1
                point[i] = 0
            else:
                break

    def get_val(point):
        val = n_arr
        for i in range(n):
            val = val[point[i]]
        return val

    # go through the N-D array
    total = functools.reduce(lambda x, y: x * y, limits)
    point = [0] * n
    res = 0
    for _ in range(total):
        val = get_val(point)
        size = [0]
        if val:
            dfs(n, n_arr, point, limits, size)
        res = max(res, size[0])
        increment_one(point)
    return res


def dfs(n, n_arr, point, limits, size):

    def get_val(point):
        val = n_arr
        for i in range(n):
            val = val[point[i]]
        return val

    def clear_val(point):
        arr = n_arr
        for i in range(n - 1):
            arr = arr[point[i]]
        arr[point[-1]] = 0

    # set to 0
    size[0] += 1
    clear_val(point)
    print(n_arr)

    # each dimension can go +1, -1
    for i in range(n):
        # + 1
        point[i] += 1
        if 0 <= point[i] < limits[i] and get_val(point):
            dfs(n, n_arr, point, limits, size)
        point[i] -= 1
        # -1
        point[i] -= 1
        if 0 <= point[i] < limits[i] and get_val(point):
            dfs(n, n_arr, point, limits, size)
        point[i] += 1


n = 3
n_arr = [
    [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [1, 0, 1, 1]
    ],
    [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0]
    ]
]

print(numIslands(3, n_arr))

