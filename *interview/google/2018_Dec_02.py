# 1. 给了若干个国家之间的汇率，比如USD GBP 0.67, GBP YEN 167, YEN EUR 0.007, 输入任意两个国家，求他们之间的汇率，
# 比如USD YEN, 输出就是0.67 * 167, 如果没有match的话输出N/A，我用了BFS，要注意就是图是双向的，因为给定USD GBP 0.67，
# 其实你同时也知道GBP USD的汇率，楼主一开始只见了单向图，最后面试官提醒了一下。
# [重複]


# 2. 给了一个M*N的矩阵，里面有些cell是block，然后给定任意两个点，要求找出一条路径，随便一条就行了，不需要最短。
# 还是图搜索的问题，BFS或者DFS就好了。
# [太簡單了]


# 3. 要求实现一个Array, 提供get(index), set(index, val), takeSnapshot(), get(index, snapshotid)。举个例子，
# set(0, 100), get(0)=100, takeSnapshot()=0001, set(0, 200), get(0)=200, get(0, 0001) = 100
import collections


class PersistKeyVal:
    def __init__(self, n):
        self.arr = [[] for i in range(n)]
        self.nxt_snap_id = 1

    def set(self, idx, val):
        if self.arr[idx] and self.arr[idx][-1][0] == self.nxt_snap_id:
            self.arr[idx][-1][1] = val
        else:
            self.arr[idx].append([self.nxt_snap_id, val])

    def get(self, idx, snapshot=-1):
        if snapshot == -1:
            if not self.arr[idx]:
                return None
            return self.arr[idx][-1][1]
        else:
            lo, hi = 0, len(self.arr[idx])
            while lo < hi:
                mi = (lo + hi) // 2
                if self.arr[idx][mi][0] <= snapshot:
                    lo = mi + 1
                else:
                    hi = mi
            print(lo)
            lo -= 1
            if lo == -1:
                return None
            else:
                return self.arr[idx][lo][1]

    def take_snapshot(self):
        self.nxt_snap_id += 1


storage = PersistKeyVal(10)
storage.set(1, 111)
storage.set(1, 312)
storage.set(1, 123)
storage.set(2, 22)
storage.set(2, 44)
storage.take_snapshot()
print(storage.get(2))
storage.set(2, 22)
print(storage.get(2))
print(storage.arr)
print(storage.get(2, 0))


# TODO: 4. 给定simple_string的定义：{string}_k, k是repeat的次数(k>1)，比如{ab}_3=ababab，给定一个正整数N，
# TODO: 求一共有多少种不同的simple_string可以构成一个长度为N的string。楼主当时是往排列组合上去想的，最后有点头绪，
# TODO: 但数学公式表达上有点混乱，没做完。
def simple_string_brute_force(n):

    def gen(n):
        res = ['']
        for i in range(n):
            tmp = []
            for s in res:
                tmp.append(s + 'a')
                tmp.append(s + 'b')
            res = tmp
        return res

    res = []
    vst = set()
    for repeat in range(2, n + 1):
        if n % repeat == 0:
            ln = n // repeat

            # generate patterns
            patterns = gen(ln)
            for pat in patterns:
                if pat * repeat not in vst:
                    res.append('{}_{}'.format(pat, repeat))
                    vst.add(pat * repeat)
    return res


print('simple string:', len(simple_string_brute_force(30)))


# def simple_string(n):


# 5. 在一个数轴上有几个点，求出到所有点的距离之和最短的点（答案可能是一个点，或者一个范围）。
def find_median_x_axis(nums):
    # init n
    n = len(nums)

    # sort the number
    nums.sort()

    if len(nums) % 2 == 1:
        return [nums[n//2]]
    else:
        return [nums[n//2-1], nums[n//2]]


print('find closest point:', find_median_x_axis([1, 2, 3, 4, 5]))
print('find closest point:', find_median_x_axis([7, 8, 1, 2, 3, 6]))


# 第二题比较开放一点，一个real time stream不停发metrics，问如何求出nth percentile的值，讨论到用bucket，
# 如何split bucket，和merge bucket in real time。

# TODO: https://stackoverflow.com/questions/48051924/how-to-approximate-90th-percentile-given-a-stream-of-millions-of-numbers
