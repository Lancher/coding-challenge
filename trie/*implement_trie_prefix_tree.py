# LEETCODE@ 208. Implement Trie (Prefix Tree)
#
# 1. Example:
#   Insert: Hey, Hit, Pig
#
#                       root = {'H', 'P'}
#                               /      \
#                              /        \
#                         {'e', 'i'}   {'i'}
#                          /      \        \
#                         /        \        \
#                      {'y'}     {'END'}   {'g'}
#                       /                    \
#                      /                      \
#                   {'END'}                  {'END'} <= `END` is the string ending flag
#
# --END--


class Trie(object):
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            # create nested dict {} to store characters
            if word[i] not in cur:
                cur[word[i]] = {}
            cur = cur[word[i]]
        cur['END'] = True

    def search(self, word):
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur:
                return False
            cur = cur[word[i]]
        # check if `END` flag found
        return 'END' in cur

    def startsWith(self, prefix):
        cur = self.root
        for i in range(len(prefix)):
            if prefix[i] not in cur:
                return False
            cur = cur[prefix[i]]
        return True
