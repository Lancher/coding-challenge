# LEETCODE@ 284. Peeking Iterator
#
# --END--


class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.next = None

    def peek(self):
        if self.next == None:
            self.next = self.iterator.next()
        return self.next

    def next(self):
        if self.next != None:
            res = self.next
        else:
            res = self.iterator.next()
        self.next = None
        return res

    def hasNext(self):
        if self.next != None:
            return True
        else:
            return self.iterator.hasNext()
