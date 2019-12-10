# 第一轮是个印度阿姨，问了一道iterator的设计题目。输入是[2,4,0,3]，实际decode后的序列是[4,4]。要求写一个迭代器，
# 实现两个函数叫next()和hasnext()来迭代返回decode后的序列。follow up是在多线程环境下如何保证正确，性能分析，
# 以及设计一个合理的后台服务来提供这样一个decoder迭代器的服务。


# 第二轮是个外国小哥哥，上来表示很不想直接问问题觉得很low，然后聊了20min简历，问了问简历上项目的一些坑。接下来问问题：
# 给一堆字符串比如[a,ab,abc,abd,acd,c]，返回最长的串，满足每个单词只比上一个单词多一个字母。
# 这个case下是a-ab-abc或者a-ab-abd
def longest_strings(words):
    # build a trie
    root = {}
    for word in words:
        cur = root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['END'] = {}

    def dfs(node, ln, res):
        if 'END' in node:
            ln += 1
        else:
            ln = 0
        res[0] = max(res[0], ln)
        for ch, nxt_node in node.items():
            dfs(nxt_node, ln, res)

    res = [0]
    dfs(root, 0, res)
    return res[0]

words = ['a', 'ab', 'abc', 'abd', 'acd', 'c']
print('longest increasing words:', longest_strings(words))



# 第三轮是个外国小姐姐，问的问题是给一个无限大的棋盘，有一个国际象棋的马（knight）每步可以走日字格，每次默认从原点出发，
# 问到一个target的坐标点（棋格）最少跳几次能到。follow up是现在封上棋盘上一些点不能跳，返回能不能到target，
# 如果能的话返回最少步数。


# 第四轮是个外国大叔，问的问题是给1-n个数，让你猜其中一个数，你每猜一个数告诉你你要猜的数和你实际猜的数比是大是小，
# 然后你需要付实际猜的那个数这么多价钱来猜一次，必须要最后能猜到那个数，不能靠排除法。
# 求问考虑最坏情况下你要付最少的钱下你要把哪个数作为第一个要猜的数。输入是n，返回也要是一个int。
# follow up是在同一个大O的情况下优化实现。
# TODO: 375. Guess Number Higher or Lower II


# 第五轮是个中国小哥，问的问题是给两个字符串A和B，你可以不断重复添加B构成一个新的字符串使得新字符串里删掉一些字母能变成A，
# 求问最少重复B几次可以构成A。比如A：azaz，B：bdacz，那么B至少重复两次变成bdaczbdacz然后删掉所有的b，d，c变成azaz。
# follow up是讨论A很长的情况下采取什么对应的策略优化，B很长的情况下采取什么策略优化。


def num_of_repeat(a, b):
    a_n = len(a)
    b_n = len(b)
    b_i = 0
    for a_i in range(a_n):
        while a[a_i] != b[b_i% b_n]:
            b_i += 1
        b_i += 1
    b_i -= 1
    return b_i // b_n + 1

print(num_of_repeat('azaz', 'bdacz'))


# 1 .高频汇率
# [做過了]


# 2. TODO: 有一堆矿，用list表示每个矿有多少吨，还有一辆车可以装X吨矿，问最少访问几次矿能装满车。
# followup 已知最少访问多少次矿，求出所有可以访问的组合。



# 3. 给2个class和一堆API node{isDirty()->bool, getChild(idx)->node, getnumofChild->int,toNodeBuilder()->nodeBuilder},
# nodeBuilder{clean()->bool, swapChild(idx,node),toNode()->node}
#  node实例是不能修改的immutable，只能通过NodeBuilder来创建。 问题是给出一个root
#  要求返回一个deep copy of root 而且原来是dirty的要变成clean

# 4.高频拿棋子
# [Mock Interview 的那提]

