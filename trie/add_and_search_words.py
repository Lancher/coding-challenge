

# LEETCODE@ 211. Add and Search Word - Data structure design
#
# Design a data structure that supports the following two operations:
class WordDictionary(object):

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node:
                node[word[i]] = {}
            node = node[word[i]]
        node['E'] = True

    def search(self, word):
        result = [False]
        self.dfs(self.root, word, 0, result)
        return result[0]

    def dfs(self, node, word, i, result):
        if result[0]:
            return
        if i == len(word):
            if 'E' in node:
                result[0] = True
        else:
            for c, next_node in node.items():

                if c == 'E':
                    continue
                if word[i] == '.' or word[i] == c:
                    self.dfs(next_node, word, i + 1, result)
