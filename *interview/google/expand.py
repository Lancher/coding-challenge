# 题目不难啊，就是括号的笛卡尔积展开 比如 "e{a, {a, b}{a, b}, c, d}d" 这种.1point3acres网
# 1. a{b, c} -> ab, ac
# 2. {a,b}{c,d} -> ac ad bc bd
# 3. a{c{a,b}} -> aca acb
# 它让你一种一种情况分开写，我各种情况都单独写了，
# 但是合并到一个最综合情况有点问题。. Waral 博客有更多文章,
# 我的纠结是 为什么不早让我考虑所有情况。。所以写的很乱
# 像{a, b}{a, b}这种， 我就DFS展开，nested我用stack从最里层开始展
# 后面想想用recursion会好写一点。。


# multiply lists
def mul_lists(l1, l2):
    res = []
    for s1 in l1:
        for s2 in l2:
            res.append(s1 + s2)
    return res


def expand(s):
    # remove all the blanks
    s = s.replace(' ', '')

    # init
    n = len(s)
    i, j = 0, 0

    # res list
    res = []
    chars = ''
    cnt = 0
    while j < n:
        if s[j] == '{':
            res.append(chars)
            chars = ''
            cnt += 1
            i = j + 1
            j += 1
            while cnt != 0:
                if s[j] == '{':
                    cnt += 1
                elif s[j] == '}':
                    cnt -= 1
                j += 1
            j -= 1
            res.append(expand(s[i:j]))
        elif s[j] == ',':
            res.append(chars)
            res.append(',')
            chars = ''
        else:
            chars += s[j]
        j += 1
    res.append(chars)

    new_res = []
    tmp = None
    for i in range(len(res)):
        if res[i] == ',':
            if tmp:
                new_res += tmp
                tmp = None
        else:
            if tmp:
                l1 = res[i] if isinstance(res[i], list) else [res[i]]
                tmp = mul_lists(tmp, l1)
            else:
                tmp = res[i] if isinstance(res[i], list) else [res[i]]
    if tmp:
        new_res += tmp

    return new_res


# print(expand('a{b,c}'))
# print(expand('a{c{a,b}efg}'))
# print(expand('{a,b}a{c,d}'))
# print(expand('{a,b}{c,d}'))
print(expand('{a,b},c'))
