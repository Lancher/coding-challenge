# Count the Inversions
#
# 1) merge sort
#
# 2) binary indexed tree
#
# 3) segment tree
#
# --END


def merge(nums, aux, lo, mi, hi, re):
    aux[lo:hi] = nums[lo:hi]

    i, j = lo, mi
    for k in range(lo, hi):
        if mi <= i:
            nums[k] = aux[j]
            j += 1
        elif hi <= j:
            nums[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            nums[k] = aux[i]
            i += 1
        else:
            nums[k] = aux[j]
            j += 1
            # [5, 2, 6, 1]
            #
            # [2, 5] [1, 6] => 2 swaps
            # [1] [2, 5] [6] => 1 shift to the head, and come over [2, 5]
            #
            # --END--
            re[0] += mi - i


# 1) merge sort
def count_inversions_mergesort(nums):
    re = [0]
    aux = nums[:]
    sz = 1
    while sz < len(nums):
        for lo in range(0, len(nums), sz * 2):
            # make sure the first part exist, so we can do the merge.
            if lo + sz < len(nums):
                merge(nums, aux, lo, lo + sz, min(lo + sz * 2, len(nums)), re)
        sz *= 2
    return re[0]


print(count_inversions_mergesort([5, 2, 6, 1]))


class BIT:
    def __init__(self, n):
        self. arr = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.arr):
            self.arr[i] += val
            i += i & -i

    def prefix_sum(self, i):
        re = 0
        while 0 < i:
            re += self.arr[i]
            i -= i & -i
        return re


# 2) binary indexed tree
def count_inversions_bit(nums):
    # make the list smaller
    d = {}
    for i, num in enumerate(sorted(list(set(nums)))):
        d[num] = i + 1

    # build bit
    bit = BIT(len(nums))

    # go from right to left
    re = 0
    for i in range(len(nums) - 1, -1, -1):
        re += bit.prefix_sum(d[nums[i]] - 1)
        bit.update(d[nums[i]], 1)
    return re


print(count_inversions_bit([5, 2, 6, 1]))


class Node:
    def __init__(self, s, e, val):
        self.s, self.e, self.val = s, e, val
        self.left, self.right = None, None


class ST:
    def __init__(self, nums):
        self.nums = nums
        self.root = self.build(0, len(nums) - 1)

    def build(self, s, e):
        if s == e:
            return Node(s, e, self.nums[s])
        elif s < e:
            m = int((s + e) / 2)
            node = Node(s, e, 0)
            node.left = self.build(s, m - 1)
            node.right = self.build(m + 1, e)
            return node
        else:
            return None

    def update(self, node, i, val):
        if not node:
            return 0

        # 1) not in the range
        if i < node.s or node.e < i:
            # RangeSum: return 0
            return 0

        # 2) we arrive the leaf
        if i == node.s == node.e:
            # RangeSum: assign the value
            node.val = val
            return node.val

        # 3) intermediate nodes
        node.val = self.update(node.left, i, val) + self.update(node.right, i, val)
        return node.val

    # RangeSum: sum()
    def sum(self, node, s, e):
        if not node:
            return 0

        # 1) not in the range
        if e < node.s or node.e < s:
            return 0

        # 2) total overlap
        if s <= node.s and node.e <= e:
            return node.val

        # 3) partial overlap
        return self.sum(node.left, s, e) + self.sum(node.right, s, e)


# 3) segment tree
def count_inversions_st(nums):
    d = {}
    for i, num in enumerate(sorted(list(set(nums)))):
        d[num] = i + 1

    st = ST(nums)
    re = 0
    for i in range(len(nums) - 1, -1, -1):
        re += st.update(st.root, i, d[nums[i]])
        st.update(st.root, 0, d[nums[i]] - 1)
    return re


print(count_inversions_st([5, 2, 6, 1]))
