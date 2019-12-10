# 第一轮： 貌似白人毛子大叔 （口音有点像毛子）
# 上来先做一个回文 isPalindrom 热热身 不到五分钟 秒掉 进入状态了以后 开始正式做题
# 围棋 找liberty cell （会下棋的同学可以理解成为 一片棋有多少口气）
# input char board[][] 棋盘 （开始问的是假设只有一片 黑/白 棋 ）
# 'b':黑棋
# 'w'： 白棋
# 'e'： 空
# output int (这片棋有多少个liberty cell)
# e.g.
# e e e e e
# e b b e e
# e w b e e. From 1point 3acres bbs
# e e e e e
#
# return 6
# 因为有六个空格 跟 这片黑棋直接相连
# 换句话说就是堵死这六个 空格 这片黑棋就死了
# 基本上就是number of islands的思路
# dfs 秒掉（10分钟写完代码吧）
# follow up 1
# 有很多片棋
# 找出每片棋的liberty cell
# 思路主要是对每片棋 做个encoding 然后一个hashmap 秒掉
# （注意算完一片棋 以后要把空格从visited set 里面删掉 因为有可能两片棋共享一个liberty cell）
# 五分钟改完代码
# follow up 2
# 问棋盘无限大 怎么办
# 用hashmap 存放过棋子的格子
# e.g.
# Map<String,char> board = new HashMap<>();
#
#
# “1,2” -> 'b'
# "3, 4" -> 'w'
#
#
# follow up 3
# 两个玩家同时玩 怎么保证 thread safe
# 典型多线程 + lock的问题
#
# follow up 4
#
# 多个玩家 同时在一个无线大的棋盘上玩
# 每对玩家初始化的时候会给定边界 （不会越界）
# 我的理解是用信号量（semaphore）做
# 第一轮到此结束 感觉不错


def liberty_cells(board):
    if not board or not board[0]:
        return 0
    m, n = len(board), len(board[0])

    # iterate the matrix
    res = []
    for i in range(m):
        for j in range(n):
            # dfs
            if board[i][j] == 'b' or board[i][j] == 'w':
                e_vst = set()
                dfs(board, board[i][j], i, j, e_vst)

                # append the block & liberty cells
                res.append((i, j, len(e_vst)))
    return res


def dfs(board, w_or_b, i, j, e_vst):
    # m, n
    m, n = len(board), len(board[0])

    # ser board to 'x'
    board[i][j] = 'x'

    # try to put empty into it
    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + x, j + y
        # empty cell
        if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'e':
            e_vst.add((ni, nj))
        if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == w_or_b:
            dfs(board, w_or_b, ni, nj, e_vst)

board = [
    ['e', 'e', 'e', 'e', 'e'],
    ['e', 'b', 'b', 'e', 'e'],
    ['e', 'w', 'b', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e']
]

print("liberty cells", liberty_cells(board))

# follow up 2
# 问棋盘无限大 怎么办
# 用hashmap 存放过棋子的格子
# e.g.
# Map<String,char> board = new HashMap<>();
#
#
# “1,2” -> 'b'
# "3, 4" -> 'w'
#
#
# follow up 3
# 两个玩家同时玩 怎么保证 thread safe
# 典型多线程 + lock的问题
#
# follow up 4
#
# 多个玩家 同时在一个无线大的棋盘上玩
# 每对玩家初始化的时候会给定边界 （不会越界）
# 我的理解是用信号量（semaphore）做
# 第一轮到此结束 感觉不错


# 第二轮
# 白人大叔 听口音应该是美国人
#
# 设计一个 data structure 存股票的价格 要求实现 . 1point3acres
# 1. 存某时间点的股票价格
# void put（long timestamp, double price）
#
# 2. 更新某时间点的股票价格 （可能因为之前存错了）
# void update(long timestamp,double price )
#
# 3. 拿到某时间点股票价格
# double get(long timestamp)
#
# 4. 拿到到目前为止的最高价格
# double getCurrentMax();
#
# 5. 删除某时间点的股票价格（可能因为之前存错了）
# void delete(long timestamp)
# 讨论过很多次了
#
# 这里就不赘述了
# 值得一提的就是 我开始就用一个正常的hashmap 存 timestamp -> price y一 treemap 来存 price -> timestamp 做的 大叔说从来没见过 这么做的 . check 1point3acres for more.
# 我用treemap主要是因为删除的时候可能删掉或者更新的时候 overwrite 当前最大 所以要重新遍历 treemap 就解决了这个问题
# 但是延长了插入时间（log n）
# 10分钟写完代码 讨论了不同的use case 跟复杂度 就完了

import heapq


class Price:

    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


class Stock:

    def __init__(self):
        self.time_price = {}
        self.max_price = []
        self.dirty = set()

    def put(self, time, price):
        if time in self.time_price:
            self.dirty.add(self.time_price[time])

        # new price
        price_obj = Price(-price)
        self.time_price[time] = price_obj
        heapq.heappush(self.max_price, price_obj)

    def get(self, time):
        if time not in self.time_price:
            return None
        return self.time_price[time].price


    def get_max_price(self):
        while self.max_price and self.max_price[0] in self.dirty:
            heapq.heappop(self.max_price)
        return None if not self.max_price else abs(self.max_price[0].price)

    def delete(self, time):
        if time in self.time_price:
            self.dirty.add(self.time_price[time])
            self.time_price.pop(time)


stock = Stock()
stock.put(10, 111)
print('stock_get_max', stock.get_max_price())
stock.delete(10)
print('stock_get_max', stock.get_max_price())
print('stock_get', stock.get(11))
stock.put(10, 111)
stock.put(10, 111)
stock.delete(10)
print('stock_get_max', stock.get_max_price())


# TODO: 第三轮
# 国人小哥
# design hashmap with expiration
# 这题地里也讨论了很多次不赘述了


# 第四轮
# 国人小哥
# decode string lc上有原题
# input string 2[ab3[cbc]]
# output string abcbccbccbcabcbccbccbc
# 括号前面是需要重复的次数 括号里面是需要重复的string
# stack 秒掉
# 小哥看了一下代码 说我写的太快了 再出一题吧
# binary tree path sum
# input binary tree node， int sum
# output boolean true（如果有path 的和等于 sum ） 反之 return false
# lc上有原题  就是一个 遍历
# 又秒掉 。还剩了20分钟 小哥说我也没准备那么多题 我们聊聊天吧 就问了问楼主现在做的东西之类的 耗一下时间。。。。. check 1point3acres for more.


def decodeString(self, s: 'str') -> 'str':
    num = ''
    chs = ''
    num_stk = []
    chs_stk = []

    # iterate the string
    for i, ch in enumerate(s):
        if ord('0') <= ord(ch) <= ord('9'):
            num += ch
        elif ch == '[':
            num_stk.append(1 if not num else int(num))
            chs_stk.append(chs)
            num = ''
            chs = ''
        elif ch == ']':
            chs = chs_stk.pop() + num_stk.pop() * chs
        else:
            chs += ch
    return chs


# 第五轮
# 压抑小胖姐姐 （很man 的一个小胖姐姐 ）
# 废话不多  先问了一个bulls and cows 刷题网的原题
# 秒掉。。。。
# 然后 问有什么好的strategy 可以尽快的猜出这个词。。。。楼主懵逼
# 说了几个解决方法 一个一个字母试 复杂度 n*256 或者 先猜出来这个词的anagram 然后排序啊
# 反正小姐姐怎么都说不行 能不能再优化。。。。
# 楼主继续拉格朗日懵逼完全不知道干嘛。。。。。
# 尴尬中结束。。。
# 然后最后还是神奇的过了。。。
def getHint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    nums = [0] * 10
    bull = cow = 0

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bull += 1
        else:
            if nums[int(secret[i])] > 0:
                cow += 1
            if nums[int(guess[i])] < 0:
                cow += 1
            nums[int(secret[i])] -= 1
            nums[int(guess[i])] += 1
    return str(bull) + 'A' + str(cow) + 'B'


# 实现三个functions， get, set, take snapshots。其实就是一个长度为N的Array。Set可以设置Index i的值，
# 每次take snapshot， version + 1，并且记录下当前version下 Array里面的值。然后get方法可以得到某一个Version下，
# 每一个Index的Array的值。就是非常Naive的方法，在Chromebook上写完了。写完之后有一个变量名Typo被指出。
# 口头跑了Test case。Follow up 时空复杂度，并且要节省空间。我的方案就是如果该Version与上一个Version相同Index相同的值不保存
# ，仅保存改变的值。写了代码后，在口头跑Case时，发现小Bug，并立马改正。
# [寫過了]



# 第二轮：看不出哪个国家。题目就是Encode a String 题目也不难。就是给了一个input String。例如aaaabbbcd => 4Xa3Xbcd的形式
# (# X char)。很快写完代码。小哥表示OK。后来又讨论了一下这个编码方式有一些问题。我举了例子，比如Input本身包含X，
# 所以编码可能就有问题，小哥说有什么办法可以避免这个问题。小哥跟我讨论了一会，小哥非常循循善诱，然后我们最后得到理想
# 的Encoding方法，并且在白板上写下了Encoding的rules，不用写代码。写完小哥说还有时间多，随手出了一道meeting room。秒之。
# e.g.
# 5xy -> yyyyy, 10
# xabc -> aaaaaaaaaabc
# 写一个encode
# function，把string
# encode成这种结构，可以做到decode(encode(string)) == string，encode之后的string应该尽量短
#
# 我就先说了下像aa这样的变成2xa会更长，所以只要对重复三次或以上的char做压缩就好。写完了代码之后，小哥说，有些corner
# cases你没有cover，我反应过来是对于原先就已经是"6xa"
# 这样的string，encode不能正确处理。于是又讨论了一下，说可以把这种情况变成"1x6xa"。



def encode(s):
    # init
    enc_s = ''
    n = len(s)

    # iterate the string
    cnt = 1
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            enc_s += str(cnt) + ':' + s[i-1]
            cnt = 1

    enc_s += str(cnt) + ':' + s[n-1]
    return enc_s


print('encoded string:', encode('aaaa:bbbcd'))


# 第四轮：是一个国人。是一道Google面筋题。就是下棋子，同行同列就可以移掉棋子。问最多可以移掉几个。我用DFS秒之。
# 后面又优化了代码。问了复杂度。小哥说我想思路想得很快，但是看起来有点紧张。后来我们就一起用中文聊天了。
# [付錢Mock的那題]
