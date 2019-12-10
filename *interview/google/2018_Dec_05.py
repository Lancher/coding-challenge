# TODO: 1. 蠡口， 其二期, 727. Minimum Window Subsequence


# 2. 经典汇率兑换，散久久
# [做過了]


# User CPU Peak
# User CPU Peak问题
# 给了一堆log，log里有用户id，resource id以resource在某个起始时间和终止时间的使用量，
# 比如 用户abc在1到5秒钟使用了CPU的数量是2，用户abc在2到3秒使用的CPU数量是4，也就是一个
# 用户对某个resource的使用在某个时间是可以叠加的， 给定一个resource id，根据用户对这个 resource的peak使用量，
# 找到top k的用户 。上面的例子中abc的CPU的peak使用量是2+4=6
# [合併]


# 1. 美国姐姐，keypad 数字对应字母，例如 2：abc, 3：def, etc, 给定一串数字，输出所有可能字母串。写得比较快，但
# 是被发现有个bug，然后分析复杂度；还做了另外一个题目，差不多难度的，抱歉我忘了具体是啥了。这轮的面试官感觉有认
# 真听我说和看我写的，感觉还比较愉快。
def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    # if the digits is empty
    if not digits:
        return []

    # table for mapping
    num_2_chrs = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    # init
    n = len(digits)
    res = [""]

    for i in range(n):
        tmp = []
        for word in res:
            for ch in num_2_chrs[digits[i]]:
                tmp.append(word + ch)
        res = tmp
    return res


# 一个打印log的系统 给了两个api：start(requestid), end(requestid), 每条log的型式：%requestid started at %startTime,
# run了多长时间。就相当于call end时要实时打印出log，但是log要求按starttime升序排列，所以如果有request开始晚但是结束早，
# 它要等之前还没结束的request结束之后才能被打印出来。楼主想法就是hashmap和双向链表（存starttime，endtime开始设成一个负数）
# ，每次call start就会往链表插入一项，但是call end时 如果不是头结点 就只更新一下endtime，如果是头结点就删除，
# 然后while下一项endtime是valid，删除下一项，把所有log都打出来。


import collections
import time


class Journal:

    def __init__(self):
        self.req_dq = collections.deque()
        self.id_req = {}

    def start(self, req_id):
        req = [req_id, time.time(), None]
        self.req_dq.append(req)
        self.id_req[req_id] = req

    def end(self, req_id):
        self.id_req[req_id][2] = time.time()
        self.flush()

    def flush(self):
        while self.req_dq and self.req_dq[0][2] is not None:
            req = self.req_dq.popleft()
            print('[Journal] {}: {}'.format(req[0], req[2] - req[1]))


journal = Journal()
journal.start(2)
journal.start(3)
journal.end(3)
journal.end(2)


# 3.中国人，题目跟decode/encode有关，具体不记得了，他自己定义了怎么encode一个interger成一个string，然后给我string,
# 让我decode。写完之后，又说如果string很大，只能一段一段读，怎么decode。这个我没写完，大概写了80%就没时间了。
# 这轮的面试官感觉很和蔼，我说啥都yes，sounds good。.


import string


alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + '-_'
al_idx = {}
for i, ch in enumerate(alphabet):
    al_idx[ch] = i


def encode(num):
    # encoded string
    enc_s = ''
    if num < 0:
        enc_s += '$'
        num = -num

    # num
    while num:
        enc_s += alphabet[num % 64]
        num //= 64
    return enc_s


def decode(s):
    if not s:
        return 0
    if s[0] == '$':
        s = s[1:]
        sign = -1
    else:
        sign = 1

    num, mul = 0, 1
    for ch in s:
        num += mul * al_idx[ch]
        mul *= 64
    return sign * num


enc_s = encode(-99999999)
print('encoded string:', enc_s)
dec_num = decode(enc_s)
print('decoded number:', dec_num)


# 美国小哥，地图上有很多building，给了他们的坐标，可能横向或者纵向相连，比如a(0,1), b(0,0), c(1,0), d(5，0)，
# 那么abc就是相连的；给定一串building id，求一共需要出building几次 比如 abcda，就是一个人要先去a, 再去b，再去c，再去d,
# 再去a，那么他需要走出building2次；这个楼主先说依次check两个building id能不能走通，面试官说太慢了；
# 然后楼主说那就想计算那些building是一堆的，不过写的时候卡了几下，那个小哥哥就很看不起的样子，一直笑，
# 弄得楼主有的紧张，后来快写完了时候，还有大概3-5分钟，他又说you just have a few minutes, be quick, hahaha。
# 弄得我又是很紧张。走之前又说，you should practice more and code faster。

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

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


def moves_bet_buildings(blds, s):
    # build mapping
    coord_idx = {}
    bldid_idx = {}
    for idx, bld in enumerate(blds):
        bld_id, i, j = bld
        coord_idx[(i, j)] = idx
        bldid_idx[bld_id] = idx

    # iterate the building again
    n = len(blds)
    uf = UnionFind(n)
    for bld_idx, i, j in blds:
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + x, j + y
            if (ni, nj) in coord_idx:
                uf.union(coord_idx[(i, j)], coord_idx[(ni, nj)])

    moves = 0
    for i in range(1, len(s)):
        if not uf.connected(bldid_idx[s[i-1]], bldid_idx[s[i]]):
            moves += 1
    return moves


buildings = [('a', 0, 1), ('b', 0, 0), ('c', 1, 0), ('d', 5, 0)]
s = 'abcda'
print('number of moves', moves_bet_buildings(buildings, s))


# 中国姐姐，已知一个interger可以分解成sum of several fibonacci number, 求证明分可以让fibonacci number个数最少。
# 小姐姐一直玩儿手机，我写完了她还在玩，我只能给她说'excuse me, do you wanna me to go through some example?',
# 她才抬起头来。
# finonacci number是指1,2,3,5,8,13这样哈
# [322. Coin Change]



# 1.面经题，左上角到右上角的path个数
def num_paths(m, n):
    # m, n
    board = [[0 for j in range(n)] for i in range(m)]

    # iterate
    for i in range(m):
        board[i][0] = 1
    for j in range(n):
        board[0][j] = 1

    # iterate the m, n
    for i in range(1, m):
        for j in range(1, n):
            board[i][j] = board[i][j-1] + board[i-1][j]

    res = 0
    for i in range(m):
        for j in range(n):
            res += board[i][j] * board[i][n-1-j]

    return res


print('number of paths:', num_paths(3, 3))


# 2.面经题，car cluster，O(N)的解想了好久，快结束时才想出来，当时看面经觉得这么简单不会考的吧
# Leetcode 853. Car Fleet
def carFleet(self, target, pos, speed):
    time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
    res = cur = 0
    for t in time[::-1]:
        if t > cur:
            res += 1
            cur = t
    return res


# 3.血崩一轮，给一个binary tree, 其中的node的child reference可以随便指向另外的node，把他变成一个valid的binary tree,
# 全程懵逼状态

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n1.right = n3
n2.left = n1
n2.right = n3
n3.left = n1
n3.right = n2


def make_binary_tree(root):
    vst = set([None])

    def dfs(node):
        vst.add(node)

        # go left
        if node.left:
            if node.left in vst:
                node.left = None
            else:
                dfs(node.left)

        # go right
        if node.right:
            if node.right in vst:
                node.right = None
            else:
                dfs(node.right)

    dfs(root)


make_binary_tree(n1)
print(n1.key)
print(n1.left)
print(n1.right)
print(n2.key)
print(n2.left)
print(n2.right)



# 4.一个简单的BFS找最短路径问题



# 第一輪：給一個 city 的左邊視角和下面視角，求最大可能 volume。
# 例如用以下 matrix 表示一個 city 每棟大樓的高度：
# [
# [1,2,2,3],
# [2,1,2,1],
# [1,1,1,1]
# ]
# 那麼左視角是 A=[3,2,1]，下視角是 B=[2,2,2,3]。給定 A 和 B（注意不是給定 matrix），回傳最大可能 volume。
# 例如單看 A 和 B 可以還原 city 為
# [
# [2,2,2,3],
# [2,2,2,2],
# [1,1,1,1]
# ]
# 可以發現粗體的部份和原 city 不相同但沒關係，所以要回傳 9+8+4=21。


def maxIncreaseKeepingSkyline(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    row, col = [0] * m, [0] * n
    for i in range(m):
        for j in range(n):
            row[i] = max(row[i], grid[i][j])
            col[j] = max(col[j], grid[i][j])

    res = 0
    for i in range(m):
        for j in range(n):
            m = min(row[i], col[j])
            res += m - grid[i][j]
    return res


# 第二輪：給一個 binary tree 和一個 ID，回傳 ID 是否在 binary tree 中。此處 ID 為 level order ID 和 node value 無關。
# 例如
#
#    1
#  2   3
# 4 5 6 7
#
# 注意當缺 node 時 ID 依然相同，例如
#
#    1
#      3
#     6 7
#
# 所以以這個例子而言如果 target ID 是 5 就要回傳 false。
#
# Solution O(logN): 由於 ID 和給定的 tree 結構無關，可以不斷把 ID 除 2 得到從 root 到此 ID 的 unique path。
# 例如 5 -> 2 -> 1 就知道一定是經過這個順序才能找到 5。得到 path 後再 traverse tree 即可。
#
# Follow up： 給一個 full binary tree，回傳此 tree 的最大 ID。


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def if_exist_in_tree(root, num):
    # empty tree
    if not root:
        return False

    # paths
    paths = []
    tmp = num
    while 1 < tmp:
        paths.append(tmp)
        tmp //= 2
    print(paths)

    # traverse
    cur = root
    while cur:
        if cur.val == num:
            return True
        nxt_val = paths.pop()
        if cur.left and cur.left.val == nxt_val:
            cur = cur.left
        elif cur.right and cur.right.val == nxt_val:
            cur = cur.right
        else:
            return False
    return False


n1 = Node(1)
n3 = Node(3)
n6 = Node(6)
n7 = Node(7)
n1.right = n3
n3.left = n6
n3.right = n7

print('if exist in a tree:', if_exist_in_tree(n1, 7))


# TODO: 第三輪：哩口七參六


# TODO: 第四輪：一個 service 每次 make request 時都會 call 一個 increment() 的 API 紀錄次數。另外 user 可以隨時 call
# get60sCount() 得到過去 60 秒的 request 次數。求 implement 這兩個 APIs。


# 1. 给两个 array of char，实现 diff 功能，就是 print 出来类似 git merge 那种 + 若干行 - 若干行的形式。
# 实质上是找出最长 common sequence，用 dp。我没有想到实际上就是 common sequence，如果想到就容易想到 dp 了。
# 最后用双 dict 实现，但是没有时间 followup。


def diff(st_chars, ed_chars):
    m, n = len(st_chars), len(ed_chars)
    dp_cnt = [[0 for j in range(n + 1)] for i in range(m + 1)]
    dp_dir = [['' for j in range(n + 1)] for i in range(m + 1)]

    for j in range(n):
        dp_dir[0][j+1] = '-'
    for i in range(m):
        dp_dir[i+1][0] = '|'

    for i in range(m):
        for j in range(n):
            if st_chars[i] == ed_chars[j]:
                dp_cnt[i+1][j+1] = dp_cnt[i][j] + 1
                dp_dir[i+1][j+1] = '`'
            else:
                if dp_cnt[i+1][j] < dp_cnt[i][j+1]:
                    dp_cnt[i+1][j+1] = dp_cnt[i][j+1]
                    dp_dir[i + 1][j + 1] = '|'
                else:
                    dp_cnt[i+1][j+1] = dp_cnt[i+1][j]
                    dp_dir[i + 1][j + 1] = '-'

    for row in dp_cnt:
        print(row)
    for row in dp_dir:
        print(row)

    # build a path
    res = []
    i, j = m, n
    while 0 < i or 0 < j:
        if i == 0:
            res.append('+' + ed_chars[j-1])
            j -= 1
        elif j == 0:
            res.append('-' + st_chars[i-1])
            i -= 1
        else:
            if dp_dir[i][j] == '`':
                res.append(st_chars[i-1])
                i, j = i - 1, j - 1
            elif dp_dir[i][j] == '-':
                res.append('+' + ed_chars[j - 1])
                j -= 1
            else:
                res.append('-' + st_chars[i - 1])
                i -= 1

    return res[::-1]


print(diff(['b', 'c', 'd'], ['a', 'b', 'c']))


# 2. 判断一个 string 是不是回文。easy 题。而且就问了这一题，因为一开始在聊天，面试官聊忘记时间了。
# [太簡單了]


# TODO: 3. 第一题 merge interval。第二题是给两个线段，用（x，y）表示起点和终点，判断这两个线段是否相交。数学题吧。
# []


# 4. bomb enemy。蠡口原题。
def maxKilledEnemies(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid or not grid[0]:
        return 0

    res = 0
    m, n = len(grid), len(grid[0])
    row, cols = 0, [0] * n
    for i in range(m):
        for j in range(n):
            # count row
            if j == 0 or grid[i][j - 1] == 'W':
                row = 0
                for k in range(n - j):
                    if grid[i][j + k] == 'W':
                        break
                    if grid[i][j + k] == 'E':
                        row += 1
            # count cols
            if i == 0 or grid[i - 1][j] == 'W':
                cols[j] = 0
                for k in range(m - i):
                    if grid[i + k][j] == 'W':
                        break
                    if grid[i + k][j] == 'E':
                        cols[j] += 1
            # put bomb
            if grid[i][j] == '0':
                res = max(res, row + cols[j])
    return res


# 5. 给一个 graph，node 是房间，link 关系是门。门有开关两个状态，每个门有对应的钥匙，有钥匙就能开门，
# 没钥匙如果门开着就能去另一个房间，否则不行。每个房间里面都有若干钥匙，如果能走到这个房间就能获得这些钥匙。
# 给起始点和终点，判断能不能走到。需要自己定义数据结构，输入输出。
# [Leecode的謀一題]


# 第一轮坐凳子问题蠡口有
import bisect
class ExamRoom:

    def __init__(self, N: 'int'):
        self.sts = []
        self.n = N

    def seat(self) -> 'int':
        if not self.sts:
            self.sts.append(0)
            return 0
        else:
            ln, idx = self.sts[0], 0
            for i in range(1, len(self.sts)):
                if (self.sts[i] - self.sts[i - 1]) // 2 > ln:
                    ln, idx = (self.sts[i] - self.sts[i - 1]) // 2, (self.sts[i] + self.sts[i - 1]) // 2
            if self.n - 1 - self.sts[-1] > ln:
                idx = self.n - 1
            bisect.insort(self.sts, idx)
            return idx

    def leave(self, p: 'int') -> 'None':
        self.sts.remove(p)

# 第二轮找到起点到终点的最佳stop set，dp解决


# 第三轮华人翻硬币问题，dp解决

# 第四轮在长方形里面随机生成一个点，终极二分查找解决
# 497. Random Point in Non-overlapping Rectangles


# 第五轮根据按键顺序得出output
# [做過了]