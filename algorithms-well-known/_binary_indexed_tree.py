# 1. the idea of binary index tree is count the prefix sum
# 2. the complement of x is -x.
# 3. https://www.youtube.com/watch?v=CWDQJGaN1gY
#
#                      0[ ]
#                ------------------
#               /   /    |         \
#              /   /     |          \
#          1[ ]  2[ ]  4[ ]        8[ ]
#                  |     ---         ---
#                  |     |  \        |  \
#                  |     |   \       |   \
#                3[ ]  5[ ]  6[ ]  9[ ]  10[ ]
#                              |
#                              |
#                              |
#                            7[ ]
#
# 4. 10 elements + 1 dummy root node
#
# 5. Get the right most bit: x & -x
#
# 6. Get the next element:
#
#   1 + 1 & (2'complement of 1) = 2
#   0001 + 0001 & (1111) = 0010
#
#   6 + 6 & (2'complement of 6) = 8
#   0110 + 0110 & (1010) = 1000
#
# 7. Get the parent element:
#
#   3 - 3 & (2'complement of 3) = 2
#   0011 - 0011 & (1101) = 0010
#
#   7 - 7 & (2'complement of 7) = 6
#   0111 - 0111 & (0111) = 0110
#
#
# --END--


class BIT:

    def __init__(self, nums):
        # n + 1 for the dummy node 0
        self.bits = [0] * (len(nums) + 1)

    def update(self, i, val):
        while i < len(self.bits):
            self.bits[i] += val
            # find next element
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.bits[i]
            # find parent element
            i -= i & -i
        return s
