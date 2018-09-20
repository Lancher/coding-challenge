# LEETCODE@ 725. Split Linked List in Parts
#
# --END--


def splitListToParts(self, root, k):
    # count the length
    ln = 0
    cur = root
    while cur:
        ln += 1
        cur = cur.next

    # count the seq length
    seq_ln = int(ln / k)
    longer_seq_num = ln - seq_ln * k

    #
    cur = root
    res = []
    for i in range(k):
        if longer_seq_num:
            n = seq_ln + 1
            longer_seq_num -= 1
        else:
            n = seq_ln
        arr = []
        for j in range(n):
            if cur:
                arr.append(cur.val)
                cur = cur.next
        res.append(arr)
    return res
