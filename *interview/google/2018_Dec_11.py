# 第一轮白人小姐姐。 题目很简单，应该是easy到medium。
# 题目就是告诉你，有一堆运动员，他们每个人身上都有号码。号码的位数可以从1 - n，n在input中给出，还给了一个 upper bound。  让你求 在这个upper bound 下 的 confusion number的个数
# confusion number 以 0，1，6，8，9为组成部分（翻转过来会造成confusion的数）。
# 比如   189 翻转过来是  981 就是一个confusion数。
# 666 翻转过来是 999 就是一个confusion数   但是  986  翻转过来是 986 就不是一个confusion数
# 以上所有条件都要你自己去探索，没有面试官会和你说。
# 还有一个限制条件是，不能以0开头（不是一个有效数）
# 不能以0结尾，因为翻转过来不是一个有效数
# 楼主一开始前20分钟想错，最后用brute force解，代码虽然写完了，但是还是漏了一种情况，这一轮非常崩，估计是weak no hire - weak hire 之间吧。


# 第二轮 语速比较快的美国小哥
# 题目的大意是有一个盗贼叫阿里巴巴，我们的目的就是要抓住它。
# 现在有一堆洞    1 2 3 4 5 6 7 8，阿里巴巴一开始可以在任意的洞内，每次他可以选择往两边逃窜。  题目的input是，一个integer 代表山洞的数量， 一个array（代表我们捕捉阿里巴巴的策略），array中每个index代表当天我们检查的山洞。
# 让我们return 这个策略是否能成功
# 比如 input：(3, [2, 2])   是return true的
# 因为阿里巴巴 一开始只可能在 1、2、3 三个山洞之间。 如果它在2，那么第一天就抓到了，如果他在1、3 那么第二天也会抓到。

def is_good(n, holes):
    robber_pos = {i for i in range(n)}
    for picK_pos in holes:
        # robber's best strategy
        robber_pos -= {picK_pos}
        print('robber\'s best strategy', robber_pos)

        # check if robber can still run
        if not robber_pos:
            return True
        else:
            nxt_robber_pos = set()
            for pos in robber_pos:
                nxt_robber_pos |= {pos - 1, pos + 1}
            robber_pos = nxt_robber_pos - {-1, n}

    return False


print('is good', is_good(3, [1, 1]))


# 第四轮 国人老哥，很亲切，面试体验也非常好
# 直接问我会不会mandarin，然后用中文面的。
# 问，给一个sorted array， 然后再给一个数，求离这个数第2大的的数，之后又拓展到第k大。
# 方法的input 如 ->  find_k_nearest(self, nums, k)
# 首先第一步是用binary search 找到离这个数最近的数（这个数不一定存在于array中）然后再去找第k大。
# 1.楼主先讲了heap的做法，时间复杂度是klgk
# 2.然后是two pointer的做法，时间复杂度是k
# 3.然后讲了一个binary seach的方法，时间复杂度是lgk
# 中间没有停顿都是秒答
# 然后老哥让我们run 了很多 binary search 的test case，都顺利的过了。
# 代码也还可以就是很多corner case，写完聊了聊，顺送了我出去。
# 这轮整体很顺畅。感觉应该是hire-strong hire之间
#
# TODO: https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC++Python-Binary-Research-O(log(N-K))


# 1）用“.”和“-”的组合给a-z进行Morse code加密，要求是最长的code要尽可能短，比如a是dot，b可以是dotdash，etc，
# 加密方法有多种，要求返回一种就可以。解法应该构造一个binary tree, 然后BFS，每一个node （. or -）
# 都有同样的两个children (. and -)。



# 2）一个binary search tree，每个node有parent link，tree里可以有duplicate，给定任何一个node （不一定是root）
# ，求这个node的in-order successor。



# 3）给一个命令 ls abc_{x, y}_c{d, e}.txt，这个命令会执行ls abc_x_cd.txt， ls abc_x_ce.txt, ls abc_y_cd.txt,
# ls abc_y_ce.txt，implement一个method将一个String （比如abc_{x, y}_c{d, e}.txt）解析成a list of Strings
# （比如abc_x_cd.txt， abc_x_ce.txt, abc_y_cd.txt, abc_y_ce.txt)。{}可以有嵌套。


# 4）假定一个code repository，很多class name，比如MyClass, AnotherClass, YourNewClass,
#                                    然后给一个CamelCase的object的名字，check这个object是不是valid，
# 比如AC, AnC, AnoC等都是valid （match AnotherClass), M也是valid (match MyClass) 但是AoC，
# YC就不valid。follow-up是如果这个repository的所有class都给定，然后会有频繁的request，应该怎么处理。
