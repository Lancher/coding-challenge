# LEETCODE 179. Largest Number
#
# --END--


class Comparable:
    # object that can be sorted thanks to magic methods.
    def __init__(self, num):
        self.value = str(num)

    def __lt__(self, other):
        # '82' is before '824' because '82|824' is greater than '824|82'
        return self.value + other.value > other.value + self.value

    def __eq__(self, other):
        return self.value + other.value == other.value + self.value


def largestNumber(self, nums):
    nums = [Comparable(n) for n in nums]
    nums.sort()
    output = ''.join((e.value for e in nums))
    return output.lstrip('0') or '0'


class Foobar:
    def __init__(self, idx):
        self.idx = idx

    def __lt__(self, other):
        """Less-than comparison."""
        return self.idx < other.idx


fooList = [Foobar(10), Foobar(2)]
fooList.sort()
print(fooList[0].idx, fooList[1].idx)   # [2, 10]

