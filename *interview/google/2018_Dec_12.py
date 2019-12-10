# 第一轮，国人小哥。给一个list of integer，问你last k integers 的均值，去吃top 10% 的数字和bottom 10% 的数字。
# return 一个list of integer，代表每一段的均值。
# 相当于第一段index range是0->k， 第二段index range是 1 -> k+1....依次类推啦


class Node:
    def __init__(self, val):
        self.val = val
        self.cnt = 1
        self.sum = val
        self.left, self.right = None, None


class BST:
    def __init__(self):
        self.root = None

    def put(self, val):
        self.root = self._put(self.root, val)

    def _put(self, node, val):
        if node is None:
            return Node(val)
        elif val <= node.val:
            node.left = self._put(node.left, val)
        else:
            node.right = self._put(node.right, val)

        node.cnt = 1 + self.cnt(node.left) + self.cnt(node.right)
        node.sum = node.sum + self.sum(node.left) + self.sum(node.right)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val == node.val:
            # find successor and delete
            if node.right is None:
                return node.left
            suc = node.right
            while suc.left is not None:
                suc = suc.left
            node.val = suc.val
            # after swapping, we delete it again
            node.right = self._delete(node.right, suc.val)
        elif val < node.val:
            node.left = self._delete(node.left, val)
        else:
            node.right = self._delete(node.right, val)

        node.count = 1 + self.cnt(node.left) + self.cnt(node.right)
        node.sum = node.sum + self.sum(node.left) + self.sum(node.right)
        return node

    def prefix_sum(self, k):
        return self._prefix_sum(self.root, 0, k)

    def _prefix_sum(self, node, smaller, k):
        print(node.val)
        cur_k = 1 + smaller + self.cnt(node.left)
        if cur_k == k:
            return node.val + self.sum(node.left)
        elif k < cur_k:
            return self._prefix_sum(node.left, 0, k)
        else:
            return node.val + self.sum(node.left) + self._prefix_sum(node.right, cur_k, k)

    def sum(self, node):
        if node is None:
            return 0
        return node.sum

    def cnt(self, node):
        if node is None:
            return 0
        return node.cnt


# [3, 1, 2, 4, 5, 11, 19, -1, 0]
bst = BST()
bst.put(3)
bst.put(1)
bst.put(2)
bst.put(4)
bst.put(5)

print(bst.root)
print(bst.prefix_sum(4), bst.prefix_sum(1))

bst.put(11)
bst.delete(3)
print(bst.prefix_sum(4), bst.prefix_sum(1))


# 第二轮，外国小哥，特别好。就是普通的dfs，找到一个有向图的最短cycle。

# 第三轮，白人小哥，表情严肃。找到两棵树的nearest common ancestor。我就想的很简单，先遍历其中一个，
# 存下来所有ancestor，然后再遍历另外一个，看有没有common。连续三个follow up, 第一个是不用递归，
# 第二个是优化每次对比是不是common ancestor的时间复杂度，第三个有没有办法不用遍历每一个节点就找到common ancestor。
# 我不知道咋写。。。。我刷题有点渣渣。


# 第四轮，白人不是小哥也不算大叔，表情更加严肃。猜数字的游戏。4位的数字，
# 每次guess一个值要给出return的score，score代表着有几个digit match上了。给你一连串的guess history.
# 要求判断某一个数有没有可能是要猜的数字。

