# LEETCODE@ 127. Word Ladder
#
# Solution 1: one way BFS
#
# Solution 2: two way BFS
#
# --END--


def ladderLength(self, beginWord, endWord, wordList):
    # 1. check if the end worf in the list
    if endWord not in wordList:
        return 0

    words = set()
    for w in wordList:
        words.add(w)
    words.add(beginWord)

    dst = 1
    q = [beginWord]
    v = {w: 0 for w in words}
    v[beginWord] = 1

    while q:
        next_q = []
        dst += 1

        for w in q:
            for i in range(len(w)):
                for j in range(ord('a'), ord('a') + 26):
                    n_w = w[:i] + chr(j) + w[i + 1:]
                    # 2. check if new string in the words
                    if n_w in words:
                        if n_w == endWord:
                            return dst
                        if not v[n_w]:
                            v[n_w] = 1
                            next_q.append(n_w)
        q = next_q
    return 0


def ladderLength(self, beginWord, endWord, wordList):
    words = set()
    for w in wordList:
        words.add(w)

    # 1. the begin word might not in the list
    words.add(beginWord)

    # 2. check if the end word in the list
    if endWord not in words:
        return 0

    q1 = [beginWord]
    q2 = [endWord]

    # set visited
    v1 = {w: 0 for w in words}
    v2 = {w: 0 for w in words}
    v1[beginWord] = 1
    v2[endWord] = 1

    dst = 2

    # 3. if q1 or q2 is empty, there is a cut inside the graph
    while q1 and q2:
        # 4. find the smaller queue to expand
        if len(q1) < len(q2):
            q, v, o_v = q1, v1, v2
        else:
            q, v, o_v = q2, v2, v1

        next_q = []
        for w in q:
            for i in range(len(w)):
                for j in range(ord('a'), ord('a') + 26):
                    n_w = w[:i] + chr(j) + w[i + 1:]
                    if n_w in words:
                        if o_v[n_w]:
                            return dst
                        else:
                            # 5. avoid loop in the graph
                            if not v[n_w]:
                                next_q.append(n_w)
                                v[n_w] = 1

        # 6. assign the next_q to original queue
        if len(q1) < len(q2):
            q1 = next_q
        else:
            q2 = next_q

        # 7. increment the dst
        dst += 1

    return 0


# LEETCODE@ 126. Word Ladder II
#
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
# from beginWord to endWord, such that:
import collections
import Queue


def findLadders(self, beginWord, endWord, wordList):
    neighbors = collections.defaultdict(set)
    min_dst = self.bfs(beginWord, endWord, wordList, neighbors)

    return self.dfs(beginWord, endWord, neighbors, min_dst)

def bfs(self, beginWord, endWord, wordList, neighbors):
    # create dict
    unvisited = set()
    for word in wordList:
        unvisited.add(word)
    unvisited.discard(beginWord)
    if endWord in unvisited:
        unvisited.discard(endWord)
    else:
        return 0

    # queue
    q1 = Queue.Queue()
    visited_s1 = set()
    q1.put(beginWord)
    visited_s1.add(beginWord)

    q2 = Queue.Queue()
    visited_s2 = set()
    q2.put(endWord)
    visited_s2.add(endWord)

    dst, min_dst = 2, None
    while not q1.empty() and not q2.empty():
        if q2.qsize() < q1.qsize():
            q1, q2 = q2, q1
            visited_s1, visited_s2 = visited_s2, visited_s1

        sz = q1.qsize()
        for _ in range(sz):
            word = q1.get()
            for i in range(len(word)):
                for j in range(97, 123):
                    new_word = word[:i] + chr(j) + word[i + 1:]

                    if new_word in visited_s2:
                        if not min_dst:
                            min_dst = dst
                        neighbors[word].add(new_word)
                        neighbors[new_word].add(word)
                    elif new_word in unvisited:
                        q1.put(new_word)
                        visited_s1.add(new_word)
                        unvisited.discard(new_word)
                        neighbors[word].add(new_word)
                        neighbors[new_word].add(word)

        dst += 1
    return min_dst if min_dst else 0

def dfs(self, beginWord, endWord, neighbors, min_dst):
    transforms = []
    transform = [beginWord]
    self.dfs_helper(beginWord, endWord, neighbors, transforms, transform, min_dst, 1)
    transform.pop()
    return transforms

def dfs_helper(self, beginWord, endWord, neighbors, transforms, transform, min_dst, dst):
    if dst == min_dst and beginWord == endWord:
        transforms.append(transform[:])
    else:
        if dst + 1 <= min_dst:
            for word in neighbors[beginWord]:
                transform.append(word)
                self.dfs_helper(word, endWord, neighbors, transforms, transform, min_dst, dst + 1)
                transform.pop()

