# TODO: 1. 给一组STRING, 要求根据这组数据，随机组成STRING， 满足：1. 首字符分布一致， 2. 尾字符分布一致，3.后面跟随的一个字
# TODO: 符也分布一致比如， ['abc', 'aefd', 'effect', 'noted' ], 首字符能是 （'a', 'e', 'n'）, 尾字符只能是（
# TODO: 'c', 'd', 't', 'd'),  'a' 后面可以跟 ('b', 'e'), 'e' 后面跟（‘f','c','d')...
# TODO: 我用HASHTABLE做的， 如何控制分布一致，我觉得是出现一次就减一次？


# 2. 给一串字符， 比如’abcde', (0,1) 属于group 1, (2,3) group 2, (4) group 3 , (0,3) group 4, 要求给出最小chunk ,
# 以及其属于的组： （0，1）： 1，4， （2，3); 2,4 ...
def min_chuck_group(s, st_eds):
    xs = []
    group_id = 1
    for i, pair in enumerate(st_eds):
        xs.append((pair[0], group_id))
        xs.append((pair[1], -group_id))
        group_id += 1

    # sort by x point
    xs.sort(key=lambda o: o[0])

    # start x from to end
    res = []
    st = set()
    j = 0
    for i in range(len(s)):
        is_changed = False
        while j < len(xs) and xs[j][0] == i:
            is_changed = True
            if xs[j][1] > 0:
                st.add(xs[j][1])
            else:
                st.remove(-xs[j][1])
            j += 1

        if is_changed:
            res.append(list(st))
    return res


s = 'abcdefg'
st_eds = [(0, 2), (2, 5), (5, 6), (6, 7), (0, 4), (4, 7)]
print('min chucks elements', min_chuck_group(s, st_eds))

# 3. Trie implement of add and search .
class Trie(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['END'] = {}

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                return False
        return 'END' in cur

    def startsWith(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch in cur:
                cur = cur[ch]
            else:
                return False
        return True


# 4. node of a BST's next bigger one
def inorderSuccessor(self, root, p):
    # successor
    suc = None

    cur = root
    while cur:
        if cur.val < p.val:
            cur = cur.right
        elif cur.val > p.val:
            suc = cur
            cur = cur.left
        else:
            # check right child's leftmost node
            if cur.right is None:
                return suc
            suc = cur.right
            while suc.left:
                suc = suc.left
            break

    return suc


# TODO 5. combine element of a increasing array  : input [1,2,2,3,4], output [1,4,3,4]
