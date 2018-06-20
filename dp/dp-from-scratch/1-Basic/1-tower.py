# TODO https://blog.csdn.net/Scythe666/article/details/50921628


# https://blog.csdn.net/nishisiyuetian/article/details/79221729
#
# 1) Solution: Top to bottom.
#
# 2) Solution: bottom to Top.
#
# --END--


def count_max_in_tower(tower):
    if not tower or not tower[0]:
        return 0
    m, n = len(tower), len(tower[0])

    for i in range(1, m):
        tower[i][0] += tower[i-1][0]
        for j in range(1, i):
            tower[i][j] += max(tower[i-1][j], tower[i-1][j-1])
        tower[i][i] += tower[i-1][i-1]
    return max(tower[m-1])


tower = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]
print(count_max_in_tower(tower))



