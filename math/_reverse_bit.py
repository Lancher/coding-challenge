# LEETCODE@ 190. Reverse Bits
#
# --END--


def reverseBits(self, n):
    bin = '{0:032b}'.format(n)
    bin = bin[::-1]
    return int(bin, 2)
